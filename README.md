 
# Instructions for using this repo

## Requirements : ubuntu system with python 3.5 installed

PWD = $HOME

## Setup Virtual environment

1. mkdir venv_chatbot 
2. virtualenv --system-site-packages -p python3 ./venv_chatbot
3. source ./venv_chatbot/bin/activate

## Install dependencies

4. pip install rasa_core
5. pip install rasa_nlu[tensorflow]
6. pip install spacy
7. python -m spacy download en_core_web_md
8. python -m spacy link en_core_web_md en
9. pip install pandas
10. git clone https://github.com/sfrpl/chatbot
11. cd chatbot/chatroom
12. yarn install
13. yarn build

## Running the code
(in the existing terminal) - T1
14. yarn serve

## Open another terminal - T2
PWD = $HOME

15. source ./venv_chatbot/bin/activate
16. cd chatbot
17. python -m rasa_core_sd.endpoint --actions action

## Open another terminal - T3
PWD = $HOME

18. source ./venv_chatbot/bin/activate
19. cd chatbot
20. python run_bot.py

## Open browser

21. Point to http://localhost:8080
22. Chat with the bot



    

    


