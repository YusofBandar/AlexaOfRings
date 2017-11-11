from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/AlexaOfRings')

@ask.intent('Hello')
def hello():
    return "hello"


@ask.launch
def launched():
    return question('Welcome to Alexa of Rings, would you like to a start')

@ask.intent('StartGame')
def startGame():
    return question('Before we begin you need to create a character')

@ask.intent('CharacterName')
def characterName():
    return question('What is you characters name and type, hobbit...dwarf...wizard?')


@ask.intent('CharacterCreated')
def characterCreated(firstname,charatype):

    return question('Hello {}, the great {}'.format(firstname, charatype))


@ask.intent('DontStartGame')
def no():
    return statement('Why did you open this app then')


if __name__ == '__main__':
    app.run(debug=True)
