from flask import Flask, render_template
from flask_ask import Ask, statement, question

app = Flask(__name__)
ask = Ask(app, '/AlexaOfRings')

playing = False;

class Character:
    name = ""
    type = ""
    health = 100
    def __init__(self):
       health = 100


CharacterList = []

@ask.launch
def launched():
    return question('Welcome to Alexa of Rings, would you like to a start')

@ask.intent('StartGame')
def startGame():
    return question('Before we begin you need to create a character')

@ask.intent('CharacterName')
def characterName():
    if(playing == False):
        return question('What is you characters name and type, hobbit...dwarf...wizard?')
    else:
        return question('You cannot create a character mid-game')


@ask.intent('CharacterCreated')
def characterCreated(firstname,charatype):
    temp = Character()
    temp.name = firstname
    temp.type = charatype
    CharacterList.append(temp)
    return question('Hello {}, the great {}, you can start adventure or create another character'.format(firstname, charatype),)


@ask.intent('DontStartGame')
def no():
    return statement('Why did you open this app then')


if __name__ == '__main__':
    app.run(debug=True)


