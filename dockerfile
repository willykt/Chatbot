# Base image (slim version for lighter images)
FROM python:3.12-slim

# Set working directory
WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libsm6 \
    libxrender1 \
    libxext6 \
    build-essential \
    cmake \
    git \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files to container
COPY . /app

# Expose port
EXPOSE 8501:8501

# Set entrypoint
CMD ["streamlit", "run", "main.py"]
