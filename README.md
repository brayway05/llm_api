# llm_api
FastAPI server for RAG project. Contains API for calling LLM inference running on my PC with GPU's.

`docker build -t llm_api .`

`docker run -p 5001:5001 llm_api`

Need a HUGGINGFACE_TOKEN in .env file to get access to llama 3.2