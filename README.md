# Simple Named Entity Recognition Service

Simple streamlit UI, utilizing a bottle.py server,showcasing the Spacy entity recognition service. Please find the instructions below to run locally or via docker compose.

# How to Run via Docker-compose

1. Clone the project repo
1. Once you have navigated to the project directory in terminal:
   On the command line: 
   1. ```docker-compose up```
   1. ```docker-compose build```
1. You will see the URL that can access the UI for the app, http://0.0.0.0:8081
1. Input text into the text box, click run analysis, and view the results of the Named Entity Recognition service

----------------------------------------------------------------------------------------------------------

# How to Run Locally: 

Make sure you are using python3

After cloning the repo, navigate into ther runLocal directory

Once in the directory, run: ```pip3 install -r requirements.txt```

# You will need to Build the UI and Service Seperately

Get the Bottle Server Started First
1. ```python3 server.py```

1. Leave this terminal open and open a new terminal window

Starting the Streamlit UI

1. In the new terminal window input ```streamlit run simpleUI.py```

You should have a browser automatically open up, but if not go to the web browser and navigate to the Local URL it shares, most likely: http://localhost:8501

1. Input text into the text box
1. Click on the button 'Run Service'
1. The text data will be sent via HTTP post to our bottle server. The bottle server utilizes spacy and runs the named entity recognition and returns the JSON result to our UI via GET which populates on the screen
