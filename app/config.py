import os

<<<<<<< HEAD
MODEL_NAME = os.getenv("MODEL_NAME", "meta-llama/Llama-3.2-3B-Instruct")
=======
GENERATOR_MODEL_NAME = os.getenv("GENERATOR_MODEL_NAME", "meta-llama/Llama-3.2-3B-Instruct")
ENCODER_MODEL_NAME = os.getenv("ENCODER_MODEL_NAME", "sentence-transformers/all-MiniLM-L6-v2")
>>>>>>> accea9112dc7623789db631088af8685ee87d0a8
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")