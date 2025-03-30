# Project Description
Named Entity Recognition (NER) is a fundamental Natural Language Processing (NLP) task that involves identifying and classifying entities such as names, organizations, locations, dates, and more within text. In this project, Transformer-based models, specifically Amaan39/btc-ner, are utilized to perform high-accuracy NER.

Several Python libraries, including NumPy, pandas, Matplotlib, PyTorch, and the Hugging Face Transformers library, are used. The input text dataset is preprocessed to make it suitable for training a transformer model. A small transformer model is developed and trained on the preprocessed dataset. Finally, distilbert-base-cased model is selected from the Hugging Face Hub and fine-tuned for named entity recognition.

A FastAPI-based REST API is implemented to extract named entities from the given input text using the Hugging Face pipeline for NER.

## Project Structure
```
Similarity-detection-using-RoBERTa/
│── notebook                # contains implementation notebook
│── app.py                  # FastAPI application
│── models.py               # Define data models using pydantic
│── predict.py              # Model inference logic
│── requirements.txt        # Dependencies

```

## How to Run
1. Clone repo
```
git clone https://github.com/amaanrzv39/NER-Transformers.git
cd NER-Transformers
```
2. Create virtual environment
```
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows
```
3. Install Dependencies
```
pip install -r requirements.txt
```
4. Start app
```
uvicorn app:app --reload
```
5. Test app
```
curl -X 'POST' 'http://127.0.0.1:8000/ner' \
     -H 'Content-Type: application/json' \
     -d '{ "text": "Elon Musk founded SpaceX in 2002 and later became the CEO of Tesla." }'
```
6. Response Format
```
{"entities":[
    {"word":"El","entity":"B-PER","start":0,"end":2,"score":0.9994},
    {"word":"##on","entity":"B-PER","start":2,"end":4,"score":0.9996},
    {"word":"Mu","entity":"I-PER","start":5,"end":7,"score":0.9995},
    {"word":"##sk","entity":"I-PER","start":7,"end":9,"score":0.9992},
    {"word":"Space","entity":"B-ORG","start":18,"end":23,"score":0.9995},
    {"word":"##X","entity":"B-ORG","start":23,"end":24,"score":0.9983},
    {"word":"Te","entity":"B-ORG","start":61,"end":63,"score":0.9997},
    {"word":"##sla","entity":"B-ORG","start":63,"end":66,"score":0.9995}
  ]
}      
```

# 📜 License

This project is open-source and available under the MIT License.