FROM python:3.10-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure Python output is flushed immediately
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Install dependencies first (Docker layer caching)
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ src/
COPY data/ data/

# Expose API port
EXPOSE 8000

# Run the FastAPI service
CMD ["uvicorn", "src.api:app", "--host", "0.0.0.0", "--port", "8000"]