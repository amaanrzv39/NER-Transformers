from fastapi import FastAPI
from predict import ner_pipeline
from models import NERRequest


app = FastAPI()

@app.post("/ner")
def perform_ner(request: NERRequest):
    if not request.text.strip():
        return {"error": "Input text cannot be empty"}

    entities = ner_pipeline(request.text)
    print(entities)

    formatted_entities = [
        {
            "word": entity["word"],
            "entity": entity["entity"],
            "start": entity["start"],
            "end": entity["end"],
            "score": round(float(entity["score"]), 4)
        }
        for entity in entities
    ]

    return {"entities": formatted_entities}
