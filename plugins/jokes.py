import random

PLUGIN = {
    "name": "tell_joke",
    "description": (
        "Tell a random programming or dad joke. Use this when the user asks for a joke."
    ),
    "parameters": {
        "type": "OBJECT",
        "properties": {},
        "required": [],
    },
}

JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "There are 10 types of people in the world: those who understand binary, and those who don't.",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "A SQL query goes into a bar, walks up to two tables and asks... 'Can I join you?'",
    "I've got a really good UDP joke to tell you, but I don't know if you'll get it.",
    "To understand what recursion is, you must first understand recursion.",
]

def run(parameters: dict, player=None, session_memory=None) -> str:
    joke = random.choice(JOKES)
    if player:
        player.write_log(f"JARVIS: {joke}")
    return joke
