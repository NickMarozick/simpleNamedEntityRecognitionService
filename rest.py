from bottle import request, response, run, post, get
import namedEntityRecognitionService
import spacy

userInput=[]
namedEntityRecognition=[]

@get("/userInput")
def getAll():
  return {"userInput":userInput}

@get('/namedEntityRecognition')
def getAll():
  return {'namedEntityRecognition': namedEntityRecognition}

@post('/userInput')
def addOne():
  #newInput= {'userText' : request.json.get('name'), 'textUserInput' : request.json.get('text')}
  newInput= {'text' : request.json.get('text')}
  #userInput.append(newInput)
  userInput.insert(0, newInput)
  return {'userInput': userInput}

@get("/analysis")
def getAnalysis():
    print(userInput[0]['text'])
    text= userInput[0]['text']
    if text:
        print(text)

        result = namedEntityRecognitionService.runAnalysis(text)
        print(result)
        return {'result': result}

    else:
        return "no text to analyze"

#@get("/refresh")
#def refresh():
#    while userInput.count()>0:
#        userInput.pop()

#    while namedEntityRecognition.count()>0:
#        namedEntityRecognition.pop()

#    return {'refreshed': 'Yes'}


run(reloader=True, debug=True)
