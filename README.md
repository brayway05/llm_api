# llm_api
FastAPI server for RAG project. Contains API for calling LLM inference running on my PC with GPU's.

`docker build -t llm_api .`

`docker run -p 5002:5002 llm_api`

Need a HUGGINGFACE_TOKEN in Dockerfile file to get access to llama 3.2