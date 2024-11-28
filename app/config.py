import os

GENERATOR_MODEL_NAME = os.getenv("GENERATOR_MODEL_NAME", "meta-llama/Llama-3.2-3B-Instruct")
ENCODER_MODEL_NAME = os.getenv("ENCODER_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")