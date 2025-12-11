# Use lean image
FROM python:3.11-slim

# Create a non-root user and a working directory
RUN useradd --create-home --shell /bin/bash appuser
WORKDIR /home/appuser/app

# Install dependencies as root then drop privileges
COPY app/requirements.txt ./requirements.txt
RUN apt-get update \
    && apt-get install -y --no-install-recommends build-essential \ \
    && pip install --no-cache-dir -r requirements.txt \
    && apt-get remove -y build-essential \ \
    && apt-get autoremove -y \ \
    && rm -rf /var/lib/apt/lists/*

# Copy application files
COPY app/main.py ./main.py

# Make sure files are owned by the non-root user
RUN chown -R appuser:appuser /home/appuser/app

# Switch to non-root user
USER appuser

EXPOSE 8000

# Run uvicorn as the non-root user
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
