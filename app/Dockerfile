# Use the official Python image from the Docker Hub
FROM python:3.9

# Set the working directory in the container
WORKDIR /app

# Copy all project files into the container (includes models, routes, etc.)
COPY . .

# Install the required dependencies
RUN pip install Flask Flask-SQLAlchemy psycopg2

# Specify the command to run the application
CMD ["python", "main.py"]
