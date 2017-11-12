from flask import Flask, render_template
from flask_ask import Ask, statement, question
import test
import random
app = Flask(__name__)
ask = Ask(app, '/AlexaOfRings')

playing = False
attacker = ""
player = -1
attacked = False

class monster:
	name = ""
	level = 5
	health = 50
	def __init__(self):
	   health = 50

class Character:
	name = ""
	type = ""
	health = 100
	stance = "NA"
	luck = random.randint(1,100);
	def __init__(self):
	   health = 100

monster1 = monster()
CharacterList = []

temp = Character()
temp.name = "Dave"
temp.type = "Hobbit"
temp.stance = "NA"
CharacterList.append(temp)

"""temp1 = Character()
temp1.name = "Amy"
temp1.type = "Wizard"
temp1.stance = "attack"
CharacterList.append(temp1)"""

@ask.launch
def launched():
	return question('Welcome to Alexa of Rings, would you like to ... start')

@ask.intent('StartGame')
def startGame():
	if(len(CharacterList) < 1):
		return question('Before we begin you need to create a character')
	else:
		value = len(CharacterList)
		return question('You have created {} characters ... you can start adventure or create another character'.format(value))

@ask.intent('CharacterName')
def characterName():
 	return question('What is your character name and type, you can be a hobbit...dwarf...wizard')


@ask.intent('CharacterCreated')
def characterCreated(firstname,charatype):
	temp = Character()
	temp.name = firstname
	temp.type = charatype
	CharacterList.append(temp)
	return question('Hello {}, the great {}, ... you can start adventure or create another character'.format(firstname, charatype))

@ask.intent('DontStartGame')
def no():
	return statement('Why did you open this app then')

@ask.intent('AdventureStart')
def adventureStart():
	playing = True
	return question('Both {} and {} start your adventure in ... Mordor ... it is time for your first battle'.format(CharacterList[0].name,CharacterList[1].name))


@ask.intent('BattleStart')
def battleStart():
	monster1.name = "Giant rat"
	return question('You are fighting a {}, {} now choose your stance'.format(monster1.name,CharacterList[0].name))

@ask.intent('ChooseStance')
def chooseStance(stance):
	if(CharacterList[0].stance == "NA"):
		CharacterList[0].stance = stance
		return question('{} you have chosen to {}, {} choose you stance'.format(CharacterList[0].name,CharacterList[0].stance,CharacterList[1].name))
	elif(CharacterList[1].stance == "NA"):
		CharacterList[1].stance = stance
		return question('{} you have chosen to {}, now to begin battle'.format(CharacterList[1].name,CharacterList[1].stance))
	return question('now to start battle')


@ask.intent('Battles')
def battles():
	global attacked
	print monster1.health
	result = ""

	if (attacked == False):
		if (monster1.health > 0 and CharacterList[0].stance != "NA" and CharacterList[1].stance != "NA"):
			if (CharacterList[0].stance == "attack"):
				CharacterList[0].luck = random.randint(1, 100);
				monster1.health = monster1.health - 20
				result = result + CharacterList[0].name + "attacks..."
			if (CharacterList[1].stance == "attack"):
				CharacterList[1].luck = random.randint(1, 100);
				monster1.health = monster1.health - 20
				result = result + CharacterList[1].name + "attacks..."
			attacked = True
			CharacterList[0].stance = "NA"
			CharacterList[1].stance = "NA"

			return question(result + ' dealing great damage, ... {} health is {}'.format(monster1.name, monster1.health))

		elif (monster1.health < 0):
			return statement('you have won battle')
		else:
			return question('need to pick stances')
	elif(attacked == True and monster1.health > 0):
		attacked = False

		choice = test.newPrediction(CharacterList[0].health,CharacterList[1].health,monster1.health,CharacterList[0].luck,CharacterList[1].luck)
		if (choice == 0):
			if(CharacterList[0].stance == "attack"):
				CharacterList[0].health = CharacterList[0].health - 10
				return question('{} attacts {}'.format(monster1.name, CharacterList[0].name))
			else:
				return question('{} defends the attack'.format(CharacterList[0].name))
		elif (choice == 1):
			if(CharacterList[1].stance == "attack"):
				CharacterList[1].health = CharacterList[1].health - 10
				return question('{} attacts {}'.format(monster1.name, CharacterList[1].name))
			else:
				return question('{} defends the attack'.format(CharacterList[1].name))
		else:
			return question('{} regen health'.format(monster1.name))
	else:

		return question('You have won the battle well done')


if __name__ == '__main__':
	app.run(debug=True)


