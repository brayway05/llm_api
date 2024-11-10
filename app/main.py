from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
from app.config import MODEL_NAME, HUGGINGFACE_TOKEN
import transformers
from app.model import get_model
from app.inference import generate_text
from pydantic import BaseModel
from huggingface_hub import login

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class LLMRequest(BaseModel):
    text: str

class LLMResponse(BaseModel):
    prediction: str

@app.on_event("startup")
def startup_event():
    print("Logging into Hugging Face Hub...")
    login(HUGGINGFACE_TOKEN)
    print("Logged In!")
    print(f"Loading model: {MODEL_NAME}...")
    get_model()
    print("Model is ready and cached!")

@app.get("/llm-inferece")
def generate_response(request: LLMRequest) -> LLMResponse:
    prediction = generate_text(input)
    return LLMResponse(prediction=prediction)