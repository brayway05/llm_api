FROM python:3.10

WORKDIR /app

ENV PYTHONPATH=/app
<<<<<<< HEAD
ENV HUGGINGFACE_TOKEN="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"
=======

ARG HUGGINGFACE_TOKEN
ENV HUGGINGFACE_TOKEN=${HUGGINGFACE_TOKEN}
>>>>>>> accea9112dc7623789db631088af8685ee87d0a8

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5002

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5002"]