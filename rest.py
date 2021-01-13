from bottle import request, response, run, post, get
import spacy

userInput=[{"name": "Entry1", "text": 25}]
namedEntityRecognition=[]

@get("/userInput")
def getAll():
  return {"userInput":userInput}

@get('/namedEntityRecognition')
def getAll():
  return {'namedEntityRecognition': namedEntityRecognition}

@post('/userInput')
def addOne():
  newInput= {'name' : request.json.get('name'), 'text' : request.json.get('text')}
  userInput.append(newInput)
  return {'userInput': userInput}

@get("/parsedDataExample")
def runSpacyTrial():
    nlp= spacy.load("en_core_web_sm")

    text = ("When Sebastian Thrun started working on self-driving cars at "
            "Google in 2007, few people outside of the company took him "
            "seriously. “I can tell you very senior CEOs of major American "
            "car companies would shake my hand and turn away because I wasn’t "
            "worth talking to,” said Thrun, in an interview with Recode earlier "
            "this week.")

    doc = nlp(text)

    # Analyze syntax
    print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
    print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

    # Find named entities, phrases and concepts
    for entity in doc.ents:
        print(entity.text, entity.label_)
        return(entity.text, entity.label_)

run(reloader=True, debug=True)
