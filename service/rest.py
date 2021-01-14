from bottle import request, response, run, post, get
import namedEntityRecognitionService
import spacy

userInput=[]

@get("/userInput")
def getAll():
  return {"userInput":userInput}


@post('/userInput')
def addOne():
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
        return {'result': 'There was no provided text to analyze'}


run(reloader=True, debug=True)
