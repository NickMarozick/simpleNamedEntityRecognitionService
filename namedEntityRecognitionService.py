import spacy



def runAnalysis(input):

  namedEntity = []

  nlp= spacy.load("en_core_web_sm")

  doc= nlp(input)

  # Analyze syntax
  print("Noun phrases:", [chunk.text for chunk in doc.noun_chunks])
  print("Verbs:", [token.lemma_ for token in doc if token.pos_ == "VERB"])

  # Find named entities, phrases and concepts
  for entity in doc.ents:
      print(entity)
      print(entity.text, entity.label_)
      newInput= {"Entity Label": entity.label_, "Entity Text": entity.text}
      namedEntity.append(newInput)

  return namedEntity
