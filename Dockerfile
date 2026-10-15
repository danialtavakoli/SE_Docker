FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py test_main.py ./

# Run the test suite when the container starts
CMD ["pytest", "-v", "test_main.py"]
