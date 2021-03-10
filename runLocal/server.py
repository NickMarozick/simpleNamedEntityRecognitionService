from bottle import request, response, run, post, get
import namedEntityRecognitionService
import spacy

userInput=[]

@get("/userInput")
def getAll():
  return {"userInput":userInput}


@post('/userInput')
def userInputPost():
  newInput= {'text' : request.json.get('text')}
  #userInput.append(newInput)
  userInput.insert(0, newInput)
  return {'userInput': userInput}


@get("/analysis")
def getAnalysis():
    if not userInput:
        return {'result': 'No user input was provided'}

    if userInput[0]['text']:
        text = userInput[0]['text']
        print(text)

        result = namedEntityRecognitionService.runAnalysis(text)
        print(result)
        return {'result': result}

    else:
        return {'result': 'There was no provided text to analyze'}

#run(host="0.0.0.0", port=8080, reloader=True, debug=True)

run(reloader=True, debug=True)

#if __name__ == "__main__":
    #run(host="0.0.0.0", port=8080, debug=True, reloader=True)
#    console.log("rest.py file accessed")
#    run(host="0.0.0.0", port=8080, reloader=True, debug=True)
