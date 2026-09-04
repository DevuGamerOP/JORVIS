# Project Requirements Document (PRD)

## Project Name
MARK LII - Personal AI Assistant

## Target Users
Developers, power users, and everyday users who want a highly customizable, cross-platform voice AI assistant capable of automating computer tasks, answering queries, managing to-do lists, and deeply integrating with their digital workflow without subscriptions.

## Goal
To build a seamless, real-time voice-activated assistant powered by the Gemini Live API that "hears, sees, understands, and controls" the user's local operating system.

## Key Features
1. **Core Voice Interaction**: Ultra-low latency voice responses using the `gemini-2.5-flash` model.
2. **System Control & Automation**: Execute desktop actions, modify OS settings, run scripts, search the web, check system metrics, manage to-do lists, and send messages through multiple platforms.
3. **Visual Awareness**: Read, capture, and explain screen elements via webcam or display.
4. **Affective Dialogue & Reactivity**: AI adapts tone based on user emotions. The HUD responds visually to real-time audio.
5. **Memory Management**: Uncapped, recallable long-term memory for identities, user preferences, and contexts without inflating token costs per request.
6. **Reversibility**: An 'Undo' stack to revert the assistant's specific OS changes.
7. **Customizability**: Configurable AI persona, UI accents, and TTS voices directly from the GUI.
8. **Plugin System**: Drop-in `.py` architecture for new features (e.g. `todo_list.py`, `jokes.py`).
