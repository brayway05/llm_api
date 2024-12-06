from app.model import get_generator_model, get_encoder_model
from transformers import pipeline
from app.config import GENERATOR_MODEL_NAME
import torch
from app.types import Message

def generate_text(text: str) -> str:
    try:
        model, tokenizer = get_generator_model()
        print("Tokenizing...")
        if tokenizer.pad_token is None:
            print("No padding token detected...Adding padding token...")
            tokenizer.pad_token = tokenizer.eos_token
        inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
        input_length = inputs.input_ids.shape[1]
        print("Generating...")
        outputs = model.generate(
            **inputs, 
            max_length=200,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            num_return_sequences=1
        )
        new_tokens = outputs[0][input_length:]
        response = tokenizer.decode(new_tokens, skip_special_tokens=True)
        return response.strip()
    except Exception as e:
        print(f"Error in generate_text: {str(e)}")
        return "I'm sorry, but I encountered an error while generating a response."
    
def pipeline_text(messages: list[Message]) -> str:
    pipe = pipeline(
        "text-generation",
        model=GENERATOR_MODEL_NAME,
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )

    messages = [{"role": msg.role, "content": msg.content} for msg in messages]

    # print("Messages: ", messages)

    outputs = pipe(
        messages,
        max_new_tokens=256,
    )

    # print("Outputs: ", outputs[0].get("generated_text"))
    return outputs[0].get("generated_text")[-1].get("content")

def encode_text(text: str) -> list[float]:
    model, tokenizer = get_encoder_model()
    print("Tokenizing...")
    if tokenizer.pad_token is None:
        print("No padding token detected...Adding padding token...")
        tokenizer.pad_token = tokenizer.eos_token
    inputs = tokenizer(text, return_tensors="pt")
    print("Encoding...")
    outputs = model(**inputs)
    embeddings = outputs.last_hidden_state.mean(dim=1).squeeze()
    return embeddings.tolist()