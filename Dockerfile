# Base image
FROM python:3.11-slim

# Set workdir
WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Optional: install browser for web tests
RUN apt-get update && apt-get install -y \
    wget curl unzip xvfb \
    chromium chromium-driver \
    && rm -rf /var/lib/apt/lists/*

# Default command to run tests
CMD ["pytest", "--maxfail=1", "--disable-warnings", "-q"]