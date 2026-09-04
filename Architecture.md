# Architecture & Technical Stack

## Technical Stack
- **Language**: Python 3.11/3.12
- **UI Framework**: PyQt6
- **LLM/AI API**: `google-genai` (Gemini 2.5 Flash and Gemini 2.5 Flash Lite)
- **Audio I/O**: `sounddevice`, `numpy`
- **Automation**: `pyautogui`, `psutil`, `playwright`, `pygetwindow`, `opencv-python`
- **Data Storage**: Local JSON files (in the `memory/` and `config/` directories)

## Core Architecture
- **`main.py`**: The primary entry point. Coordinates the audio capture loops, Gemini Live WebSocket session, event hooks, and tool routing.
- **`ui.py`**: Handles all frontend PyQt6 visualization (HUD, System Monitors, Chat Logs, Dialog/Overlays).
- **`core/`**: Critical runtime logic (e.g., prompt instruction definition, safe action confirmation gates, audio device enumeration, and plugin loaders).
- **`actions/`**: Isolated scripts defining the tools the AI uses (e.g., file processing, search, desktop control).
- **`plugins/`**: Drop-in folder for extending the assistant. Each Python file here acts as a zero-configuration AI tool module.
- **`memory/`**: Managers for both ephemeral session tokens and persistent long-term knowledge saving.
