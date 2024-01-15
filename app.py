from flask import Flask, render_template, url_for, request, redirect
from transformers import pipeline, Conversation
import chatter



app = Flask(__name__)

blender = chatter.chatbot()

@app.route('/', methods = ['POST', 'GET'])
def index():
    #conversation = Conversation()
    if request.method == 'POST':
        task_content = request.form['chat']

        responses = blender.talk(task_content)

        inputs = blender.conversation.past_user_inputs

        length = list(range(len(responses)))

        return render_template('index.html', responses = responses, inputs = inputs, length = length)
    else:
        return render_template('index.html')



@app.route('/model/<int:modelid>', methods = ['POST'])
def change_model(modelid):
    #blender.change_to_model2()
    return render_template('index.html')

    



if __name__ == "__main__":
    app.run(debug=True)