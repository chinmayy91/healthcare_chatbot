import random

# Define a dictionary of healthcare-related questions and answers
healthcare_qa = {
    "What are the symptoms of COVID-19?": "Common symptoms of COVID-19 include fever, cough, and difficulty breathing. Other symptoms may include fatigue, loss of taste or smell, and body aches.",
    "How can I schedule a doctor's appointment?": "To schedule a doctor's appointment, you can call our main office number or use our online booking system on our website.",
    "What should I do if I'm experiencing a medical emergency?": "If you're experiencing a medical emergency, please call 911 or go to the nearest emergency room immediately.",
    "How often should I get a physical exam?": "It's generally recommended to get a physical exam once a year, but this may vary based on your age, health condition, and risk factors. Consult with your doctor for personalized advice.",
    "What are the visiting hours for the hospital?": "Our general visiting hours are from 9 AM to 8 PM daily. However, these may vary for different departments or under special circumstances.",
    "How can I access my medical records?": "You can access your medical records through our patient portal. If you need assistance, please contact our medical records department.",
    "What insurance plans do you accept?": "We accept a wide range of insurance plans. Please check our website or contact our billing department for a complete list of accepted insurance providers.",
    "How can I refill my prescription?": "You can refill your prescription by calling our pharmacy department, using our mobile app, or visiting our website.",
    "What should I bring to my first appointment?": "Please bring a valid ID, your insurance card, a list of current medications, and any relevant medical records or test results from previous healthcare providers.",
    "How do I prepare for a blood test?": "For most blood tests, you'll need to fast for 8-12 hours beforehand. Drink plenty of water and avoid strenuous exercise before the test. Your doctor will provide specific instructions if needed.",
    "ok": "Please go ahead and ask questions."
}

def healthcare_chatbot():
    print("Welcome to the Healthcare Chatbot. How can I assist you today?")
    print("(Type 'quit' to exit)")

    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input == 'quit':
            print("Thank you for using the Healthcare Chatbot. Take care!")
            break
        
        best_match = None
        best_score = 0
        
        for question in healthcare_qa:
            score = sum(word in question.lower() for word in user_input.split())
            if score > best_score:
                best_score = score
                best_match = question
        
        if best_match and best_score > 0:
            print(f"Chatbot: {healthcare_qa[best_match]}")
        else:
            print("Chatbot: I'm sorry, I don't have information on that topic. Please try rephrasing your question or ask about a different healthcare-related topic.")

if __name__ == "__main__":
    healthcare_chatbot()
