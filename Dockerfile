FROM python:3.10-slim

WORKDIR /app

ENV PYTHONPATH=/app
ENV HUGGINGFACE_TOKEN="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"

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "5001"]