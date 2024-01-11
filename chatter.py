from transformers import pipeline, Conversation

model_tag = "facebook/blenderbot-400M-distill"

chatbot = pipeline(model = model_tag)

conversation = Conversation()

def talk(words):
    print(type(words))
    conversation.add_user_input(words)
    conversation = chatbot(conversation)
    return conversation.generated_responses[-1]

