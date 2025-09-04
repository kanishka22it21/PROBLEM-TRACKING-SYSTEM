# Use official Python base image
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install dependencies
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Flask port
EXPOSE 5000

# Start Flask app
CMD ["python", "app.py"]
