# Use Python as the base image
FROM python:3.8-slim-buster

# Install pip and Python dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1


# Set the working directory in the container
WORKDIR /app


# Install pip requirements
COPY /requirements.txt .
RUN python3 -m pip install -r requirements.txt

# Copy main application file
COPY generateData.py .

# Set the port for the application
ENV PORT=5000
EXPOSE 5000

# Command to run the application
CMD ["python3", "generateData.py"]