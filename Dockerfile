FROM python:3.10

WORKDIR /app

RUN pip install --no-cache-dir -r uvicorn fastapi transformers

COPY . .

EXPOSE 5001

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5001"]