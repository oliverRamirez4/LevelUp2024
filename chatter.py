
from transformers import pipeline, Conversation


# Utility classs for handling the chatbot
class chatbot():
        
    def __init__(self):
        self.model = pipeline("text2text-generation", model="facebook/blenderbot-400M-distill")
        self.user_inputs = []
        self.model_outputs = []
    #takes string as a parameter and returns the response from the chat bot.
    def talk(self, user_input):
        self.user_inputs.append(user_input)
        response = self.model(user_input)[0]['generated_text']
        self.model_outputs.append(response)
        return self.model_outputs
    
boss = chatbot()

print (boss.talk("hello"))


    
        
    
        
