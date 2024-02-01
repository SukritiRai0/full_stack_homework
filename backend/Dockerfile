# Use an official Python runtime as a parent image
FROM python:3.11-slim

# Set the working directory to /usr/src/app
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Install Flask and Flask-SQLAlchemy
RUN pip install Flask Flask-SQLAlchemy

# Install the retry module
RUN pip install retry

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "run.py"]