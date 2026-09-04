# Project Phases

## Phase 1: Core Foundation & Communication
- Set up local environment, UI foundations (PyQt6), and Gemini API connections.
- Implement reliable local microphone and speaker interactions with low latency.
- Achieve basic conversational loops.

## Phase 2: Automation & Operating System Hooks
- Implement OS system monitors (CPU, Memory, Network, Temps).
- Build actions for system manipulation: File system access, web browsing, screen capturing, launching applications.
- Develop the "Undo" feature for OS modifications.

## Phase 3: Memory & Context
- Build localized JSON data persistence.
- Program logic that allows the AI to implicitly search past facts (using a tool limit index).
- Automatically summarize the previous session upon shutdown.

## Phase 4: Customization & Extensibility
- Construct the Plugins architecture for easy drop-in expansions (`todo_list`, `jokes`).
- Add the UI customization menu (UI colors, dynamic name/voice changing).
- Optimize system latencies and refine code models.
