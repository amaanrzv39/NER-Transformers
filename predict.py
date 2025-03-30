from dotenv import load_dotenv
from transformers import pipeline


load_dotenv()

ner_pipeline = pipeline("ner", model="Amaan39/btc-ner", tokenizer="Amaan39/btc-ner")
