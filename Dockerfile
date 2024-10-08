# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy everything into the container
COPY . .

# Install any needed Python packages
RUN pip install --no-cache-dir --upgrade -r requirements.txt

# Default command
CMD ["python", "main.py"]