[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)    
# VidAI

VidAI is a Python desktop application that generates structured notes from online videos using Gemini AI. It features a simple graphical user interface (GUI) built with Tkinter, lets you choose your preferred note-taking style and Gemini model, and saves your notes to a file. The app handles video downloading, AI interaction, and note formatting automatically.

<img src="https://github.com/user-attachments/assets/aab89f72-6a93-4cae-be7b-d1779b03abe9" alt="VidAI Demo" width="1000"/>

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

## Additional Notes

- The app uses `yt-dlp` to download videos and Gemini AI for note generation.
- Only public video URLs supported by `yt-dlp` can be processed.
- Your API key is stored locally in the `.env` file.
- **Be cautious:** Generated notes are based on AI interpretation and may not be 100% accurate.
