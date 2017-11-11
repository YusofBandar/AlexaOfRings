from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/AlexaOfRings')

@ask.intent('Hello')
def hello():
    return "hello"


@ask.launch
def launched():
    return question('Welcome to Alexa of Rings, would you like to a start game')

@ask.intent('StartGame')
def yes():
    return question('Before we begin you need to create a character')

@ask.intent('CharacterName')
def characterName():
    return question('What is you characters name?')


@ask.intent('CharacterCreated')
def characterCreated(Names):
    return question('You have created a character... do you want to create another character or start adventure')

@ask.intent('test')

@ask.intent('DontStartGame')
def no():
    return statement('Why did you open this app then')


if __name__ == '__main__':
    app.run(debug=True)
