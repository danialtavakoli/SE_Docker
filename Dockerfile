FROM python:3.x
WORKDIR /app
COPY . .
CMD ["python", "test_main.py"]
