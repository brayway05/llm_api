from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import GENERATOR_MODEL_NAME, ENCODER_MODEL_NAME, HUGGINGFACE_TOKEN
from app.model import get_generator_model, get_encoder_model
from app.inference import generate_text, encode_text, pipeline_text
from huggingface_hub import login
from app.types import EncodeRequest, DecodeRequest, LLMResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"]
)

@app.on_event("startup")
def startup_event():
    print("Logging into Hugging Face Hub...")
    login(HUGGINGFACE_TOKEN)
    print("Logged In!")
    print(f"Loading models: {GENERATOR_MODEL_NAME} and {ENCODER_MODEL_NAME}...")
    get_generator_model()
    get_encoder_model()
    print("Models are ready and cached!")

@app.post("/generate")
def generate_response(request: DecodeRequest) -> LLMResponse:
    print(f"Generating response for: {request.messages[-1].content}")
    prediction = pipeline_text(request.messages)
    return LLMResponse(prediction=prediction)

@app.post("/encode")
def encode_request(request: EncodeRequest) -> list[float]:
    print(f"Encoding text: {request.text}")
    return encode_text(request.text)
     