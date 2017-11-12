# Alexa Of Rings

Alexa of Rings is a text-based game that is controlled through the medium of speech using the Alexa Voice SDK. The SDK is interacted with through the Amazon Echo. The inspiration for this project came from looking at MUD games and realising that there are not a great deal of games that accessible to the visually impaired and even less that both those with visual impairments and those without can play together.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

The following dependencies need to be installed and setup before you can test the game.

```
Python 2.x
ngrok server
```

#### Installing Prerequisites

How to install the dependencies mentioned above.

To install Python 2.x go to the [Python download page](https://www.python.org/downloads/) and select the latest version of Python 2. Follow the instructions within the setup executable program to correctly install Python.

To setup the ngrok server go to the [ngrok download page](https://ngrok.com/download) and select the appropriate version for your machine. Once downloaded unzip the folder and open ngrok.exe. 
A command prompt will open where you type in:
```
ngrok http 5000
```
After doing this you will see two urls; one will be a http url and the other will be a https enabled url.
