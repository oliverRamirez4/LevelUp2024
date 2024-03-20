from flask import Flask, render_template, url_for, request, redirect
from transformers import pipeline, Conversation
import chatter



app = Flask(__name__)

# the chatbot class to allow functionality with hugging face model
blender = chatter.chatbot()

#Flask app
@app.route('/')
def start():
    return render_template('index.html')

#Route for when the user submits text to the model
@app.route('/chat', methods = ['POST'])
def index():
    # All requests should be POST requests. There are no GET requests in the app
    if request.method == 'POST':

        try:
            task_content = request.form['chat']

            #process the chat with the chatbot
            blender.talk(task_content)

            #all chatbot responses
            responses = blender.model_outputs

            #all chatbot inputs 
            inputs = blender.user_inputs

            #For iterating through response and inputs with jinja
            length = list(range(len(responses)))

            return render_template('index.html', responses = responses, inputs = inputs, length = length)
        
        except:
            return render_template('index.html', responses = ["An Error occured with the Hugging face model"], inputs = [], length = 1)

        
    else:
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)