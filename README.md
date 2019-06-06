# Rasa Chat bot
This repo contains code  as well as the data used for training a rasa chat bot. The front end used is https://github.com/scalableminds/chatroom frontend. The bot also has functionality of picking data and time using duckling.


## Requirements : 
 * python 3.6.7
 * rasa 1.0.1 
 * https://github.com/scalableminds/chatroom v0.10.x as front end


## Functionality of the code
```
* Chatbot to talk with user and setup an appointment with some speciality in a hospital
* The availability of the doctor is controlled by # DocAvail.csv
* This mimics the presence of a database where information is present and the input of the user can be cross checked with the data present
* Once the user enters the data, if no doctor is available the chatbot will reply back and ask the user to enter the details again
* If the doctor is available , appointment is scheduled

```


## Instructions for Installation
```

PWD = $HOME

## Setup Virtual environment

1. mkdir venv_chatbot 
2. virtualenv --system-site-packages -p python3 ./venv_chatbot
3. source ./venv_chatbot/bin/activate

## Install dependencies


4. pip install -f requirements.txt
5. pip install spacy
6. python -m spacy download en_core_web_md
7. python -m spacy link en_core_web_md en
8. pip install pandas
9. git clone https://github.com/sfrpl/chatbot
10. git clone https://github.com/scalableminds/chatroom
11. cd chatroom
12. yarn install

## Running the code
(in the existing terminal) - T1

15. yarn serve
### Before running 15 ensure the current working directory is $/chatbot/chatroom

## Open another terminal - T2

PWD = $HOME
16. source ./venv_chatbot/bin/activate
17. cd chatbot
18. make run-actions
### Before running 18 ensure the current working directory is $/chatbot

## Open another terminal - T3

PWD = $HOME
16. source ./venv_chatbot/bin/activate
17. cd chatbot
18. make run-core
### Before running 18 ensure the current working directory is $/chatbot



## Open another terminal - T4
19. source ./venv_chatbot/bin/activate
20. cd chatbot
21. Install docker
22. docker run -p 8000:8000 rasa/duckling


## Open browser

23. Point to http://localhost:8080
24. Chat with the bot

```



    

    


