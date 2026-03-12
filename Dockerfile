FROM python:3.11-slim

# Install dependencies for Chrome
RUN apt-get update && apt-get install -y \
    wget unzip curl gnupg fonts-liberation libnss3 libx11-xcb1 \
    libxcomposite1 libxdamage1 libxrandr2 libasound2 libatk1.0-0 \
    libcups2 libgtk-3-0 libxss1 libgbm1 --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Install Google Chrome
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

# Install ChromeDriver matching Chrome
RUN CHROME_VERSION=$(google-chrome --version | grep -oP "\d+\.\d+\.\d+") \
    && wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$CHROME_VERSION/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /app
WORKDIR /app

# Default command
CMD ["pytest"]