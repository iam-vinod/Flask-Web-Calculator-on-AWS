FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy and install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application files
COPY app/ .

# Expose port 5000 (default Flask port)
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
