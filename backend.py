from dotenv import load_dotenv
from pathlib import Path
from google import genai
from enum import Enum
import shutil
import yt_dlp
import json
import time
import os

load_dotenv()
GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY")
TEMP_VIDEOS_PATH: Path = Path('tmpVids')

GEMINI_MODELS: tuple = ('gemini-2.5-pro',
                'gemini-2.5-flash',
                'gemini-2.5-flash-lite',
                'gemini-2.0-flash',
                'gemini-2.0-flash-lite')

class NoteTakingMethod(Enum):
    CONCISE = 'concise'
    SIMPLE = 'simple'
    BULLET_POINTS = 'bullet_points'
    DETAILED = 'detailed'
    OUTLINE = 'outline'
    SUMMARY = 'summary'

    def getPrompt(self) -> str:
        with open('note-taking-prompts.json', 'r') as jsonFile:
            methods = json.load(jsonFile)

        for method in methods:
            if method['method'] == self.value:
                return method['prompt']
            
    def getPrettyString(self) -> str:
        if self == NoteTakingMethod.CONCISE:
            return 'Concise'
        elif self == NoteTakingMethod.SIMPLE:
            return 'Simple'
        elif self == NoteTakingMethod.BULLET_POINTS:
            return 'Bullet Points'
        elif self == NoteTakingMethod.DETAILED:
            return 'Detailed'
        elif self == NoteTakingMethod.OUTLINE:
            return 'Outline'
        elif self == NoteTakingMethod.SUMMARY:
            return 'Summary'

def convertPrettyStringToMethod(prettyString: str) -> NoteTakingMethod | None:
    mapping = {
        'Concise': NoteTakingMethod.CONCISE,
        'Simple': NoteTakingMethod.SIMPLE,
        'Bullet Points': NoteTakingMethod.BULLET_POINTS,
        'Detailed': NoteTakingMethod.DETAILED,
        'Outline': NoteTakingMethod.OUTLINE,
        'Summary': NoteTakingMethod.SUMMARY
    }
    return mapping.get(prettyString, None)

def setApiKey(api_key: str) -> None:
    apiKey: str = api_key
    with open('.env', 'w') as envFile:
        envFile.write(f'GEMINI_API_KEY={apiKey}\n')
    load_dotenv(override=True)

def isApiKeySet() -> bool:
    return not (GEMINI_API_KEY == '' or GEMINI_API_KEY is None)

def clearTmp() -> None:
    tmpPath: Path = Path('tmp')
    if tmpPath.exists():
        shutil.rmtree(tmpPath)

def download(url: str) -> tuple[bool, Path]:
    '''
    Download a video from a URL using yt-dlp.

    Returns:
        tuple[bool, Path]: A tuple containing a boolean indicating success or failure, and the path to the downloaded video file (if successful).
    '''

    ydlOptions: dict = {'outtmpl': str(TEMP_VIDEOS_PATH / 'vidOut.%(ext)s')}

    with yt_dlp.YoutubeDL(ydlOptions) as ydl:
        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f'Error downloading video from url "{url}": {e}')
            clearTmp()
            return (False, None)

    infoDict = ydl.extract_info(url, download=False)
    videoExt = infoDict.get('ext', None)
    if videoExt:
        videoPath = TEMP_VIDEOS_PATH / f'vidOut.{videoExt}'
        return (True, videoPath)
    else:
        print(f'Error: Video title or extension not found.')
        clearTmp()
        return (False, None)

def waitForActive(client: genai.Client, fileObj, timeout: float = 30.0) -> bool:
    '''
    Waits until the uploaded file is ACTIVE or times out.

    Returns:
        bool: True if the file became ACTIVE in time, False otherwise.
    '''

    start = time.time()
    while time.time() - start < timeout:
        fileStatus = client.files.get(name=fileObj.name)
        if getattr(fileStatus, "state", None) == "ACTIVE":
            return True
        time.sleep(1)
    return False

def takeNotes(url: str, method: NoteTakingMethod=NoteTakingMethod.SIMPLE, model: str = 'gemini-2.5-flash-lite') -> str:
    '''
    Takes notes from a video file.

    Args:
        url (str): The URL of the video.
        method (NoteTakingMethod): The method to use for taking notes.

    Returns:
        str: The notes taken from the video.
    '''

    success, videoPath = download(url)

    if success:
        SYSTEM_PROMPT: str = ('You are VidNotes, an AI assistant designed to watch videos and produce notes.'
                            'Your primary goal is to accurately capture, summarize, and structure key information from the video content.'
                            'You must strictly follow the note-taking method described below when generating your output. Do not deviate from the specified style, level of detail, tone, or structure.'
                            'Note-Taking Method:'
                            f'{method.getPrompt()}'
                            'Your response should only contain the notes according to the inserted method — no extra commentary, explanations, or deviations.')
        
        client: genai.Client = genai.Client(api_key=GEMINI_API_KEY)

        print('Uploading video to AI...')
        videoFile = client.files.upload(file=str(videoPath))
        print('Upload complete.')

        if not waitForActive(client, videoFile):
            print(f'Error: File {videoFile.name} did not become ACTIVE in time.')
            clearTmp()
            return None

        print('Generating notes...')
        response = client.models.generate_content(
            model=model,
            contents=[videoFile, SYSTEM_PROMPT])
        print('Notes generated successfully.')
        
        clearTmp()

        return response.text
    else:
        return None

if __name__ == '__main__':
    videoURL: str = 'https://www.youtube.com/watch?v=4qGrteTY1EM'
    notes: str = takeNotes(videoURL, NoteTakingMethod.SIMPLE)
    print(f'\n{notes}')

    with open('notes.txt', 'w') as f:
        f.write(notes)