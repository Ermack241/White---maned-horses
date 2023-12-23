FROM python:3.9-slim

WORKDIR /app

RUN pip install Flask==0.10.1 &&/
    cd /app && pip install -r requirements.txt

COPY . .
CMD ["python", "app.py"]