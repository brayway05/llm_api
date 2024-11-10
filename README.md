# llm_api
FastAPI server for RAG project. Contains API for calling LLM inference running on my PC with GPU's.

`docker build --build-arg HUGGINGFACE_TOKEN="Key here" llm-api .`

`docker run -p 5002:5002 llm-api`
