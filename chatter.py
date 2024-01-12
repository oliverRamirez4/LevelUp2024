from transformers import pipeline, Conversation

class chatbot():
    model = pipeline(model = "facebook/blenderbot-400M-distill")
        
    def __init__(self):
        self.conversation = Conversation()

    def talk(self, user_input):
        self.conversation.add_user_input(user_input)
        self.conversation = self.model(self.conversation)
        return self.conversation.generated_responses
    
        
    
        
