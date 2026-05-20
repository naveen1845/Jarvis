# Jarvis Voice Assistant

A Python-based AI voice assistant for macOS using speech recognition, Gemini AI, and text-to-speech.

## Features

- Wake word activation ("Jarvis")
- Voice command recognition
- Gemini AI integration
- Open websites
- Play music from custom library
- macOS native text-to-speech
- Conversational responses

## Technologies Used

- Python
- SpeechRecognition
- Google Gemini API
- python-dotenv
- macOS `say` command

## Project Structure

```text
project/
│
├── src/
│   ├── main.py
│   ├── musicLibrary.py
│   └── ...
│
├── .env
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

### 1. Clone Repository

```bash
git clone <your_repo_url>
cd <project_name>
```

### 2. Create Virtual Environment

```bash
python3 -m venv .venv
```

### 3. Activate Environment

```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Create `.env`

Create a `.env` file in the root directory:

```env
GOOGLE_API_KEY=your_api_key_here
```

### 6. Run Application

```bash
python src/main.py
```

## Notes

- Designed for macOS
- Uses native `say` command for speech output
- `.env` and `.venv` are excluded from Git tracking