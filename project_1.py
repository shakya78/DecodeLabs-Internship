responses = {
    "hello": "Hey there! 👋 How can I help you today?",
    "hi": "Hello! 😊 Nice to meet you.",
    "hey": "Hey! What's up?",

    "how are you": "I'm doing great! Thanks for asking.",
    "how are you?": "I'm doing great! Thanks for asking.",

    "who are you": "I'm RuleBot, a rule-based AI chatbot.",
    "what is your name": "My name is RuleBot.",

    "what can you do": """
I can respond to:
• Greetings
• AI questions
• Machine Learning questions
• Jokes
• Small talk
• Help commands
""",

    "what is ai": "Artificial Intelligence is the simulation of human intelligence by machines.",

    "what is artificial intelligence": "Artificial Intelligence is the simulation of human intelligence by machines.",

    "what is machine learning": "Machine Learning allows computers to learn patterns from data.",

    "what is a chatbot": "A chatbot is a program designed to simulate conversation with humans.",

    "tell me a joke": "Why do programmers prefer dark mode? Because light attracts bugs! 😂",

    "good morning": "Good Morning! ☀️",
    "good afternoon": "Good Afternoon! 😊",
    "good evening": "Good Evening! 🌙",

    "thanks": "You're welcome!",
    "thank you": "Happy to help!",

    "help": """
Available Commands:
- hello
- how are you
- who are you
- what is ai
- what is machine learning
- what is a chatbot
- tell me a joke
- bye
"""
}

EXIT_COMMANDS = {"bye", "exit", "quit", "goodbye"}

print("🤖 RuleBot Started!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    if user_input in EXIT_COMMANDS:
        print("Bot: Goodbye! 👋")
        break

    response = responses.get(
        user_input,
        "Sorry, I don't understand that. Type 'help' for available commands."
    )

    print("Bot:", response)