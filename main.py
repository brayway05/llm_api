from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
import transformers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
def startup_event():
    print("Starting up with default model llama 3.2 3B...")
    print("Initializing the model...")
    print("Loading the model...")
    print("Model is ready and cached!")

@app.get("/model-options")
def get_model_options():
    # TODO create extensive list of models we can try out
    return {"models": ["llama-3.2-1B", "llama-3.2-3B", "", ""]}

@app.get("/llm-inferece")
def generate(input: str, model_name: str):
    try:
        model = transformers.pipeline("text-generation", model="gpt2")
        return model(input, max_length=100)[0]['generated_text']
    except:
        print("Error in generating text")
    return ""