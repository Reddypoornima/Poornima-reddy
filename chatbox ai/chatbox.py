def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello"]:
            print("Chatbot: Hi there! How can I help you?")
        
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm doing great! How about you?")
        
        elif "your name" in user_input:
            print("Chatbot: I'm ChatBot, your virtual assistant.")
        
        elif "help" in user_input:
            print("Chatbot: Sure, I'm here to help. You can ask me about our services, hours, or location.")
        
        elif "services" in user_input:
            print("Chatbot: We offer web development, app development, and AI solutions.")
        
        elif "location" in user_input:
            print("Chatbot: We are located in New York City.")
        
        elif "hours" in user_input or "timing" in user_input:
            print("Chatbot: Our working hours are 9 AM to 6 PM, Monday to Friday.")
        
        elif user_input in ["bye", "exit", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
