from flask import Flask, render_template, url_for, request, redirect
from transformers import pipeline, Conversation



app = Flask(__name__)

#Managing the model
model_tag = "facebook/blenderbot-400M-distill"
chatbot = pipeline(model = model_tag)






@app.route('/', methods = ['POST', 'GET'])
def index():
    conversation = Conversation()
    if request.method == 'POST':
        task_content = request.form['chat']
        conversation.add_user_input(task_content)
        conversation = chatbot(conversation)
        response = conversation.generated_responses[-1]
        return render_template('index.html', response = response)
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)