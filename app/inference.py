from app.model import get_model

def generate_text(text: str) -> str:
    # TODO: optimize this a bit for better responses and error handling
    model, tokenizer = get_model()
    inputs = tokenizer(text, return_tensors="pt")
    outputs = model.generate(**inputs, max_length=200)
    prediction = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return prediction