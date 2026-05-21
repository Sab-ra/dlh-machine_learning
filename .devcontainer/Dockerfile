FROM python:3.9-slim-focal

# System tools + glow (terminal markdown renderer)
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gnupg \
    wget \
    mysql-client default-mysql-client \
    && curl -fsSL https://repo.charm.sh/apt/gpg.key \
        | gpg --dearmor -o /etc/apt/keyrings/charm.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" \
        > /etc/apt/sources.list.d/charm.list \
    && wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add - \
    && echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list \
    && apt-get update && apt-get install -y glow mongodb-org-shell \
    && rm -rf /var/lib/apt/lists/*

# matplotlib in headless mode (no GUI window - save figures to files instead)
ENV MPLBACKEND=Agg

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
