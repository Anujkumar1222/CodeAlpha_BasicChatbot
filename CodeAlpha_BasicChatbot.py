def chatbot():
    print("🤖 ChatBot: Hello! Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("🤖 ChatBot: Hi! Nice to meet you.")
        
        elif user == "how are you":
            print("🤖 ChatBot: I'm fine, thanks for asking!")
        
        elif user == "what is your name":
            print("🤖 ChatBot: My name is CodeAlpha Bot.")
        
        elif user == "help":
            print("🤖 ChatBot: You can say hello, ask my name, or ask how I am.")
        
        elif user == "bye":
            print("🤖 ChatBot: Goodbye! Have a great day.")
            break
        
        else:
            print("🤖 ChatBot: Sorry, I don't understand that.")

# Run chatbot
chatbot()