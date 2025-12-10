FROM python:3.14-slim

WORKDIR /app

# Install system deps for some packages
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libxml2-dev \
    libxslt1-dev \
    gcc \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./
RUN python -m pip install --upgrade pip setuptools wheel && pip install --no-cache-dir -r requirements.txt

COPY . /app

CMD ["/bin/bash"]
