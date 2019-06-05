 
#Instructions for using this repo

Requirements : ubuntu system with python 3.6.7 installed
Works with rasa 1.0.1 with https://github.com/scalableminds/chatroom v0.10.x as front end

Setup Virtual environment

1. mkdir venv_chatbot 
2. virtualenv --system-site-packages -p python3 ./venv_chatbot
3. source ./venv_chatbot/bin/activate

Install dependencies

4. pip install -f requirements.txt
5. pip install spacy
6. python -m spacy download en_core_web_md
7. python -m spacy link en_core_web_md en
8. pip install pandas
9. git clone https://github.com/sfrpl/chatbot
10. git clone https://github.com/scalableminds/chatroom

Open Another Terminal 
11. cd chatroom
12. yarn install
13. yarn serve
14. make run
15. Open index.html and chat in browser. Speech recognition yet to be tested



    

    


