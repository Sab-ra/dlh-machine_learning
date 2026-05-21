FROM python:3.13-slim

# Install system tools, glow, MySQL client, and MongoDB shell (mongosh)
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gnupg \
    wget \
    default-mysql-client \
    && mkdir -p /etc/apt/keyrings \
    && curl -fsSL https://repo.charm.sh/apt/gpg.key | gpg --dearmor -o /etc/apt/keyrings/charm.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" > /etc/apt/sources.list.d/charm.list \
    && curl -fsSL https://www.mongodb.org/static/pgp/server-7.0.asc | gpg --dearmor -o /etc/apt/keyrings/mongodb.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/mongodb.gpg] http://repo.mongodb.org/apt/debian bookworm/mongodb-org/7.0 main" > /etc/apt/sources.list.d/mongodb-org-7.0.list \
    && apt-get update \
    && apt-get install -y glow mongodb-mongosh \
    && rm -rf /var/lib/apt/lists/*

# Create a 'mongo' alias for 'mongosh' so old curriculum commands still work flawlessly
RUN ln -s /usr/bin/mongosh /usr/local/bin/mongo

# matplotlib in headless mode (no GUI window - save figures to files instead)
ENV MPLBACKEND=Agg

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
