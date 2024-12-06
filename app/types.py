from pydantic import BaseModel

class Message(BaseModel):
    role: str
    content: str

class DecodeRequest(BaseModel):
    messages: list[Message]

class EncodeRequest(BaseModel):
    text: str

class LLMResponse(BaseModel):
    prediction: str