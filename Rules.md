# Rules & Constraints

## Technical Boundaries
1. **Dependencies**: Prefer built-in Python libraries and OS-native integrations to limit cross-platform bloat, but leverage mature libraries (e.g. `psutil`, `pyautogui`) when necessary.
2. **Models**: Always use `gemini-2.5-flash` for high-reasoning tasks and `gemini-2.5-flash-lite` where applicable. Never revert to deprecated API versions.
3. **Audio Handling**: Do not freeze or hang the main UI thread. Keep async task queues properly buffered and clear of strict memory leaks. Audio latency MUST stay as low as possible (e.g. 50ms buffer chunks max when writing back TTS to speakers).
4. **Action Gates**: Any irreversible change (restarting PC, turning off WiFi) MUST pass through `core/confirm.py` and require physical user confirmation on the UI.
5. **Plugin Architecture**: A plugin must adhere to the `_template.py` design, declaring a unique `name` and specific schema properties. The `run` function should return strings indicating completion or specific user-facing errors.

## AI Persona Guidelines
- You are JARVIS (or whatever custom name the user provided).
- Reply as quickly and efficiently as possible.
- Be concise and direct. Do not read the actual tool tags out loud.
- Never confirm an irreversible action as "done" before the user presses the confirm button.
