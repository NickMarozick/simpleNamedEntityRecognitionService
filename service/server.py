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
  print(newInput)
  #userInput.append(newInput)
  userInput.insert(0, newInput)
  return {'userInput': userInput}


@get("/analysis")
def getAnalysis():
    print(userInput)
    print(userInput[0]['text'])
    text= userInput[0]['text']
    if text:
        print(text)

        result = namedEntityRecognitionService.runAnalysis(text)
        print(result)
        return {'result': result}

    else:
        return {'result': 'There was no provided text to analyze'}


run(host="0.0.0.0", port=8080, reloader=True, debug=True)


#if __name__ == "__main__":
#    run(host="0.0.0.0", port="8080", debug=True, reloader=True)

    #run(reloader=True, debug=True)
