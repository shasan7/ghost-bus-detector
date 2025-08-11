# 1. Use official Python image
FROM python:3.11-slim

# 2. Set work directory
WORKDIR /app

# 3. Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy backend code
COPY . .

# 5. Expose backend port
EXPOSE 8000

# 6. Run FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
