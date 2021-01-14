# nick-1700

Thank you for your time reviewing my work. 

# How to Run: 

Make sure you are using python3 

After cloning the repo, run: 'pip3 install -f requirements.txt'

# You will need to Build the UI and Service Seperately 

Get the Bottle Server Started First
1) 'cd service' 
2) python3 server.py

3) Leave this terminal open and open a new terminal window

Starting the Streamlit UI
1) 'cd ..'
2) 'cd ui' 
3) streamlit run simpleUI.py

You should have a browser automatically open up, but if not go to the web browser and navigate to http://localhost:8501

4) Input text into the text box 
5) Click on the button 'Run Service' 
6) The text data will be sent via HTTP post to our bottle server. The bottle server utilizes spacy and runs the named entity recognition and returns the JSON result to our UI via GET which populates on the screen

# To Do:

- in /service, update the Dockerfile so that it successfully creates the docker image for our bottle server and runs properly
- With both working Dockerfiles, implement Docker compose to use "docker-compose up" for the initial project build
