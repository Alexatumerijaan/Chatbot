# Use an official Python runtime as the base image
FROM python:3.8-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the application dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Define the environment variable
ENV PORT 5000

# Expose the port 5000
EXPOSE 5000

# Define the command to run the application
CMD ["/bin/sh", "-c", "python -m Main"]
