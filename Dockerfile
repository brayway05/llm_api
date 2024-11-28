FROM python:3.10

WORKDIR /app

ENV PYTHONPATH=/app

ARG HUGGINGFACE_TOKEN
ENV HUGGINGFACE_TOKEN=${HUGGINGFACE_TOKEN}

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5002"]