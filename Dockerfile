# Dockerfile
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install OS dependencies
RUN apt-get update && apt-get install -y gcc build-essential

# Copy files
COPY . .

# Install Python dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Dagster needs this ENV var
ENV DAGSTER_HOME=/app/dagster_home

# Create dagster_home directory
RUN mkdir -p /app/dagster_home

# Expose Dagster web port
EXPOSE 3000

# Entrypoint for Dagster web server
CMD ["dagster", "dev", "-h", "0.0.0.0", "-p", "3000"]
