from app.model import get_generator_model, get_encoder_model

def generate_text(text: str) -> str:
    # TODO: optimize this a bit for better responses and error handling
    model, tokenizer = get_generator_model()
    print("Tokenizing...")
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    print("Generating...")
    outputs = model.generate(**inputs, max_length=200)
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

def encode_text(text: str) -> list[float]:
    model, tokenizer = get_encoder_model()
    print("Tokenizing...")
    inputs = tokenizer(text, return_tensors="pt")
    print("Encoding...")
    outputs = model(**inputs)
    return outputs.last_hidden_state[0].detach().numpy().tolist()