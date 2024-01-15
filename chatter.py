from transformers import pipeline, Conversation, AutoTokenizer

class chatbot():
        
    def __init__(self):
        self.conversation = Conversation()
        self.model = pipeline(model = "facebook/blenderbot-400M-distill", tokenizer=AutoTokenizer.from_pretrained("facebook/blenderbot-400M-distill"))

    def talk(self, user_input):
        self.conversation.add_user_input(user_input)
        self.conversation = self.model(self.conversation)
        return self.conversation.generated_responses


    
        
    
        
