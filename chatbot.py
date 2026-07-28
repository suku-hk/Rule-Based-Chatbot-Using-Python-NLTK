import random
import nltk 
from nltk.stem import PorterStemmer
from data import data

#initialize NLTK and download required resources
nltk.download("punkt")

stemmer = PorterStemmer()


#Map intent categories to their corresponding intent categories
INTENT_RESPONSE_MAP ={
    "greetings" : "responses",
    "farewells" : "farewell_responses",
    "questions" : "question_responses",
    "small_talk": "small_talk_responses"
}

def preprocess(sentence):
    tokens = nltk.word_tokenize(sentence.lower())
    return [stemmer.stem(token) for token in tokens]


def get_response(user_input):
    processed_input = preprocess(user_input)

    # Check all the pattern categories
    for intent_category, response_category in INTENT_RESPONSE_MAP.items():
        for pattern in data[intent_category]:
            processed_pattern = preprocess(pattern)

            if all(word in processed_input for word in processed_pattern):
                return random.choice(data[response_category])

    # Fall back for unknown inputs
    return "I'm not sure how to respond to that. Could you rephrase that?"

def chat():
    print("Chatbot: Hello , I'm your friendly chatbot.Type 'exit' to end the conversation.")
   
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() =="exit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Chatbot : {response}")
        
        
if __name__ == "__main__" :
    chat()        
            
            
               
