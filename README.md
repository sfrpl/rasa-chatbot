 
#Instructions for using this repo

Requirements : ubuntu system with python 3.5 installed

Setup Virtual environment

1. mkdir venv_chatbot 
2. virtualenv --system-site-packages -p python3 ./venv_chatbot
3. source ./venv_chatbot/bin/activate

Install dependencies

4. pip install rasa_core
5. pip install rasa_nlu[tensorflow]
6. pip install spacy
7. python -m spacy download en_core_web_md
8. python -m spacy link en_core_web_md en
9. pip install pandas
10. git clone https://github.com/sfrpl/chatbot

    

    


