# Use official Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (to leverage Docker cache)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Run FastAPI server
CMD ["uvicorn", "application.main:app", "--host", "0.0.0.0", "--port", "8000"]
