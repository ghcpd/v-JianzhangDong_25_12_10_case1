FROM python:3.14-slim

WORKDIR /app

# Install build tools and dependencies then install project requirements
COPY requirements.txt ./
RUN python -m pip install --upgrade pip setuptools wheel \
    && pip install --no-cache-dir -r requirements.txt

# Copy the project source
COPY . /app

# Default entry — run the test runner script
CMD ["bash", "./run_test.sh"]
