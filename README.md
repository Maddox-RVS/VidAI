# VidAI

**Transform videos into intelligent notes with AI**

VidAI is a powerful Python desktop application that automatically converts online videos into structured, intelligent notes using Google Gemini AI. Whether you're a student capturing lecture content, a professional documenting meetings, or a researcher extracting insights from video materials, VidAI streamlines the note-taking process with advanced AI technology.

## ✨ Key Features

- 🤖 **AI-Powered Analysis**: Leverages Google Gemini AI for accurate video content understanding
- 📝 **6 Note-Taking Styles**: Choose from Concise, Simple, Bullet Points, Outline, Detailed, or Summary formats
- 🎬 **Universal Video Support**: Works with any video URL supported by yt-dlp (YouTube, Vimeo, and more)
- 🖥️ **User-Friendly GUI**: Clean, intuitive Tkinter interface with real-time processing updates
- ⚡ **Multiple AI Models**: Support for latest Gemini models (2.5-pro, 2.5-flash, 2.0-flash variants)
- 💾 **Local Processing**: Secure local storage with automatic temporary file cleanup
- 🔧 **Easy Setup**: Simple API key management through GUI or environment files

<!-- <img src="" alt="VidAI Demo" width="1000"/> -->

## Prerequisites

Before using VidAI, ensure you have the following:

1. **Python:** The program requires **Python (3.13.5 or newer recommended)**. Download Python from [python.org](https://www.python.org).
2. [Anaconda or Miniconda](https://www.anaconda.com/docs/main) (recommended for managing environments).
3. [Git](https://git-scm.com/) (for cloning the repository).
4. A valid **Gemini API Key** from Google AI Studio.

## Setup

To set up VidAI, follow these steps:

1. **Clone the repository using git:**

   ```bash
   git clone https://github.com/Maddox-RVS/VidAI.git
   cd VidAI
   ```

2. **Create and activate a conda environment (recommended):**

   ```bash
   conda create -n vidai python=3.13.5
   conda activate vidai
   ```

3. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

## Setting Up Your Gemini API Key

1. Go to [Google AI Studio](https://ai.google.dev/) and create a Gemini API key.
2. Run the application and click the "Set API Key" button in the GUI, then paste your key when prompted.
3. Alternatively, you can manually add your key to the `.env` file:

   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## Usage

To use VidAI:

1. Run the application:

   ```bash
   python main.py
   ```

2. Enter the video URL in the provided field.
3. Select your preferred note-taking style and Gemini model from the dropdown menus.
4. Click "Generate Notes" to start processing.
5. When finished, choose where to save your notes as a `.txt` file.

## 📋 Note-Taking Styles

VidAI offers six distinct note-taking approaches to match your specific needs:

| Style | Description | Best For |
|-------|-------------|----------|
| **Concise** | Ultra-brief, essential points only | Quick reference, key takeaways |
| **Simple** | Beginner-friendly, plain language | General understanding, accessible content |
| **Bullet Points** | Well-structured, organized lists | Easy scanning, presentation materials |
| **Outline** | Hierarchical format with headings | Academic notes, structured learning |
| **Detailed** | Comprehensive, thorough documentation | Research, in-depth analysis |
| **Summary** | High-level paragraph summaries | Executive briefings, overviews |

## 📌 Additional Information

### Technical Details
- Built with Python 3.13.5+ for optimal performance
- Uses `yt-dlp` for robust video downloading from major platforms
- Powered by Google Gemini AI for intelligent content analysis
- Temporary files are automatically cleaned up after processing

### Supported Platforms
- ✅ YouTube, Vimeo, and other yt-dlp compatible sites
- ✅ Windows, macOS, and Linux operating systems
- ✅ Various video formats and resolutions

### Privacy & Security
- 🔒 API keys stored locally in `.env` files
- 🗑️ Temporary video files automatically deleted
- 📱 No cloud storage of personal content
- 🛡️ Secure local processing only

### Important Notes
- **Accuracy**: Generated notes are AI-powered and may not be 100% accurate
- **Internet Required**: Active connection needed for video download and AI processing
- **API Limits**: Subject to Google Gemini AI usage limits and pricing