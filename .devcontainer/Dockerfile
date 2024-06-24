FROM python:3.9-slim

# Install necessary packages
RUN apt-get update && apt-get install -y \
    libpq-dev gcc

# Set work directory
WORKDIR /workspace

# Install Python dependencies
COPY src/requirements.txt /workspace/requirements.txt
RUN pip install -r /workspace/requirements.txt

# Copy the application files
COPY src /workspace/src

# Expose port
EXPOSE 8000
