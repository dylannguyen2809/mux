from flask import Flask, request, jsonify
import openai
import os
import twilio.twiml

app = Flask(__name__)

# configure openai api key
openai.api_key = 'YOUR_OPENAI_API_KEY'

@app.route('/handle_call', methods=['GET', 'POST'])
def handle_call():
    """
    Endpoint for receiving voice calls from Twilio and handling the call using OpenAI's voice assistant
    """

    # stream the audio data from twilio
    # https://www.twilio.com/docs/voice/tutorials/voice-receiving#streaming-audio
    # https://github.com/twilio/twilio-python/blob/master/twilio/rest/Client.py
    # https://github.com/twilio/twilio-python/issues/452
    # https://stackoverflow.com/questions/56451501/how-to-stream-audio-from-twilio-in-python
    # https://stackoverflow.com/questions/56014549/streaming-audio-from-twilio-in-python-flask-app
    return 0

def get_news():
    """
    Function to get the latest news using AI web scraper, as a string output/JSON object
    """

    return 0

def get_user_data():
    """
    Function to get user data from a file called users.csv
    """
    user_data = []
    
    return user_data

if __name__ == '__main__':
    app.run(debug=True)
