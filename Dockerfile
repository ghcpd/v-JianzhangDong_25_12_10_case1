# Dockerfile to replicate the environment
FROM python:3.14-slim

# Install OS deps for building wheels (if needed)
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential libxml2-dev libxslt1-dev zlib1g-dev libssl-dev libffi-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip setuptools wheel
RUN pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

# Create non-root user
RUN useradd -m appuser && chown -R appuser /app
USER appuser

ENV PATH="/home/appuser/.local/bin:$PATH"

CMD ["python", "-u", "-c", "import os; print('Container ready. Run tests with run_test.sh inside container or call python tests/*.py')"]
