import os

GENERATOR_MODEL_NAME = "meta-llama/Llama-3.2-1B-Instruct"
# GENERATOR_MODEL_NAME = "distilbert/distilgpt2"
ENCODER_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")