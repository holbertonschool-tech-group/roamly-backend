FROM python:3.9

WORKDIR /app

COPY app .

RUN pip install Flask Flask-SQLAlchemy psycopg2

CMD ["python", "main.py"]
