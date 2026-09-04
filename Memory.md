# Memory & Context (Live)

**Current Status:**
- The project runs on the MARK LII architecture.
- Gemini API endpoints have been successfully updated to standard `gemini-2.5-flash` variants.
- Audio latency has been dramatically reduced from ~200ms buffering to ~50ms (`9600 bytes` reduced to `2400 bytes` threshold).
- Custom logic features via Plugins (`todo_list.py` and `jokes.py`) have been established and checked for syntax.
- App initialization delays (`pyautogui` waits) inside `actions/send_message.py` have been padded to support robust app boot speeds (e.g. 5.0 seconds wait for WhatsApp to spin up).

**Outstanding Notes:**
- UI components load Xvfb cleanly for local background validation in tests.
- When expanding future plugins, ensure the `import` statements strictly handle directory nesting (using `memory/` or `config/` properly).
