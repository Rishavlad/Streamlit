
rules = {
    "hello": "Hello! How can I assist you with your automotive needs today?",
    "hi": "Hi there! What can I help you with regarding cars or services?",
    "car models": "We offer a wide range of car models including sedans, SUVs, trucks, and electric vehicles. Do you have a specific type in mind?",
    "new car": "Are you interested in a specific make or model for a new car purchase?",
    "used car": "We have a great selection of certified pre-owned vehicles. What are you looking for?",
    "service": "We provide various services including oil changes, tire rotations, brake inspections, and major repairs. What service do you need?",
    "appointment": "To schedule an appointment, please visit our website or call our service department at XXX-XXX-XXXX.",
    "financing": "We offer flexible financing options. Would you like to know more about our loan or lease programs?",
    "hours": "Our dealership is open from 9 AM to 7 PM on weekdays, and 10 AM to 5 PM on Saturdays. We are closed on Sundays.",
    "location": "We are located at 123 Auto Avenue, Carville. You can find directions on our website.",
    "test drive": "Great! To schedule a test drive, please let us know which model you are interested in and your preferred date and time.",
    "parts": "We stock genuine parts for various makes and models. Please specify the part you are looking for.",
    "trade-in": "We offer competitive trade-in values for your current vehicle. Would you like to get an appraisal?",
    "electric vehicle": "Electric vehicles are a great choice! We have models like the Electra Sedan and the Volt SUV. Are you interested in the range or charging details?",
    "thank you": "You're welcome! Is there anything else I can assist you with?",
    "bye": "Goodbye! Drive safely and we hope to see you soon!",
    "exit": "Goodbye! Drive safely and we hope to see you soon!"
}

def get_response(user_input):
    """
    Matches user input to a predefined rule and returns a response.
    """
    user_input = user_input.lower()
    for keyword, response in rules.items():
        if keyword in user_input:
            return response
    return "I'm sorry, I don't understand. Could you please rephrase or ask about car models, services, or appointments?"

print("Welcome to the Automotive Chatbot! Type 'exit' or 'bye' to quit.")

while True:
    user_message = input("You: ")
    if user_message.lower() in ["exit", "bye"]:
        print(get_response(user_message))
        break
    else:
        bot_response = get_response(user_message)
        print(f"Bot: {bot_response}")
