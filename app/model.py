from transformers import AutoModelForCausalLM, AutoTokenizer
from app.config import MODEL_NAME

model = None
tokenizer = None

def get_model():
    global model, tokenizer
    if model is None or tokenizer is None:
        model_name = MODEL_NAME
        model = AutoModelForCausalLM.from_pretrained(model_name)
        tokenizer = AutoTokenizer.from_pretrained(model_name)
    return model, tokenizer
