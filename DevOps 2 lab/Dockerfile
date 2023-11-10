FROM python:latest

RUN cd /app
RUN pip install Flask==0.10.1
RUN pip install -r requirements.txt


COPY app /app
CMD ["python", "app.py"]