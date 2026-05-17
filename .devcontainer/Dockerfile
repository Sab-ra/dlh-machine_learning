FROM python:3.13-slim

# System tools + glow (terminal markdown renderer)
RUN apt-get update && apt-get install -y \
    git \
    curl \
    gnupg \
    && curl -fsSL https://repo.charm.sh/apt/gpg.key \
        | gpg --dearmor -o /etc/apt/keyrings/charm.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" \
        > /etc/apt/sources.list.d/charm.list \
    && apt-get update && apt-get install -y glow \
    && rm -rf /var/lib/apt/lists/*

# matplotlib in headless mode (no GUI window - save figures to files instead)
ENV MPLBACKEND=Agg

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
