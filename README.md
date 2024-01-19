# Level Up Project 2024
I built this project while participating in the Colorado College Level Up Program during January 2024. The prompt that I chose to do was, "Build a website that allows users to generate outputs from a pre-trained model." I built a website that allows users to interact with a conversational model and get generated responses.

## Description
This web app was built using Flask, Hugging Face transformers, HTML, and SCSS. It was my first time working with flask and hugging face transformers. The user inputs their message in the input box and then presses send. This sends a POST http request to the flask application which returns the response of the pre-trained conversational model. The model is the [facebook/blenderbot-400M-distill](https://huggingface.co/facebook/blenderbot-400M-distill?text=Hey+my+name+is+Julien%21+How+are+you%3F) on hugging face.
