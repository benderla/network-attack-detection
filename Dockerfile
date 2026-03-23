FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY src/ src/

COPY data/ data/

CMD ["python", "src/attack_detection_model.py"]

CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]