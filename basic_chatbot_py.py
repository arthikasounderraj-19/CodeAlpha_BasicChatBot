def chatbot():
    print("=" * 50)
    print(" WELCOME TO BASIC CHATBOT ")
    print("=" * 50)
    print("Type 'bye' to exit the chatbot.\n")
    while True:
        user = input("You: ").lower().strip()
        if user == "hello" or user == "hi":
            print("Bot: Hello! Nice to meet you.")
        elif user == "how are you":
            print("Bot: I'm doing great! Thanks for asking.")
        elif user == "what is your name":
            print("Bot: My name is CodeAlpha ChatBot.")
        elif user == "who created you":
            print("Bot: I was created using Python for the CodeAlpha Internship.")
        elif user == "what can you do":
            print("Bot: I can answer simple questions and chat with you.")
        elif user == "python":
            print("Bot: Python is a popular programming language.")
        elif user == "thank you" or user == "thanks":
            print("Bot: You're welcome!")
        elif user == "good morning":
            print("Bot: Good Morning! Have a wonderful day!")
        elif user == "good night":
            print("Bot: Good Night! Sweet dreams!")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day.")
            break
        else:
            print("Bot: Sorry! I don't understand that.")
chatbot()
