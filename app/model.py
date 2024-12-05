from transformers import AutoModelForCausalLM, AutoTokenizer, AutoModel
from app.config import GENERATOR_MODEL_NAME, ENCODER_MODEL_NAME

generator_model = None
generator_tokenizer = None
encoder_model = None
encoder_tokenizer = None

def get_generator_model():
    global generator_model, generator_tokenizer
    if generator_model is None or generator_tokenizer is None:
        
        generator_model = AutoModelForCausalLM.from_pretrained(GENERATOR_MODEL_NAME)
        generator_tokenizer = AutoTokenizer.from_pretrained(GENERATOR_MODEL_NAME)
    return generator_model, generator_tokenizer

def get_encoder_model():
    global encoder_model, encoder_tokenizer
    if encoder_model is None or encoder_tokenizer is None:
        encoder_model = AutoModel.from_pretrained(ENCODER_MODEL_NAME)
        encoder_tokenizer = AutoTokenizer.from_pretrained(ENCODER_MODEL_NAME)
    return encoder_model, encoder_tokenizer
