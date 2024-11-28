from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os
from app.config import GENERATOR_MODEL_NAME, ENCODER_MODEL_NAME, HUGGINGFACE_TOKEN
from app.model import get_generator_model, get_encoder_model
from app.inference import generate_text, encode_text
from pydantic import BaseModel
from huggingface_hub import login

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"]
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
    print(f"Loading models: {GENERATOR_MODEL_NAME} and {ENCODER_MODEL_NAME}...")
    get_generator_model()
    get_encoder_model()
    print("Models are ready and cached!")

@app.get("/generate")
def generate_response(request: LLMRequest) -> LLMResponse:
    print(f"Generating response for: {request.text}")
    prediction = generate_text(request.text)
    return LLMResponse(prediction=prediction)

@app.get("/encode")
def encode_request(request: LLMRequest) -> list[float]:
    print(f"Encoding text: {request.text}")
    return encode_text(request.text)
     