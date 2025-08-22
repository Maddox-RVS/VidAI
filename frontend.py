from tkinter import simpledialog
from tkinter import filedialog
from tkinter import ttk
from tkinter import *
import backend

def getStyleOptions() -> list[str]:
    styles: list[str] = []
    for method in backend.NoteTakingMethod:
        styles.append(method.getPrettyString())
    return styles

def getModelOptions() -> list[str]:
    models: list[str] = []
    for model in backend.GEMINI_MODELS:
        models.append(model)
    return models

def onPressSetApiKey() -> None:
    apiKey = simpledialog.askstring("Set API Key", "Enter your API key:")
    if apiKey:
        backend.setApiKey(apiKey)
        print("API Key set successfully.")

def onPressGenerateNotes() -> None:
    urlLabel.config(text='Enter URL:')
    url = urlTextbox.get("1.0", "end").strip()
    style = styleVar.get()
    model = modelVar.get()

    if not url:
        print("Please enter a video URL.")
        return

    generateButton.config(text='Generating...', state='disabled')
    setApiKeyButton.config(state='disabled')
    root.update()

    try:
        notes = backend.takeNotes(url, backend.convertPrettyStringToMethod(style), model)
        print(f"Generated Notes:\n{notes}")

        if notes:
            filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if filePath:
                with open(filePath, "w", encoding="utf-8") as notesFile:
                    notesFile.write(notes)
                print(f"Notes saved to {filePath}")
    except Exception as e:
        print(f"Error generating notes: {e}")
        urlLabel.config(text='Enter URL (An error occurred, make sure your API key is set correctly and that the url is compatible):')
    finally:
        generateButton.config(text='Generate Notes', state='normal')
        setApiKeyButton.config(state='normal')
        root.update()

root = Tk()
root.title('Video Note Taker')
root.geometry('550x225')

mainFrame = ttk.Frame(root, padding=10)
mainFrame.grid(sticky='nsew')
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
mainFrame.grid_columnconfigure(0, weight=1)
mainFrame.grid_columnconfigure(1, weight=1)

urlLabel = ttk.Label(mainFrame, text='Enter URL:')
urlLabel.grid(row=0, column=0, columnspan=2, sticky='w')

urlTextbox = Text(mainFrame, width=40, height=3)
urlTextbox.grid(row=1, column=0, columnspan=2, sticky='ew')

styleLabel = ttk.Label(mainFrame, text='Style:')
styleLabel.grid(row=2, column=0, sticky='ew', pady=(10,0))

styleOptions: list[str] = getStyleOptions()
styleVar = StringVar(value=styleOptions[0])
styleDropdown = ttk.OptionMenu(mainFrame, styleVar, styleOptions[0], *styleOptions)
styleDropdown.grid(row=2, column=1, sticky='ew', pady=(10,0))

modelLabel = ttk.Label(mainFrame, text='Model:')
modelLabel.grid(row=3, column=0, sticky='ew', pady=(10,0))

modelOptions: list[str] = getModelOptions()
modelVar = StringVar(value=modelOptions[0])
modelDropdown = ttk.OptionMenu(mainFrame, modelVar, modelOptions[0], *modelOptions)
modelDropdown.grid(row=3, column=1, sticky='ew', pady=(10,0))

generateButton = ttk.Button(mainFrame, text='Generate Notes')
generateButton.grid(row=4, column=0, columnspan=2, pady=10, sticky='ew')
generateButton.config(command=onPressGenerateNotes)

setApiKeyButton = ttk.Button(mainFrame, text='Set API Key')
setApiKeyButton.grid(row=5, column=0, columnspan=2, pady=(0,10), sticky='ew')
setApiKeyButton.config(command=onPressSetApiKey)

root.mainloop()