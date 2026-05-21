FROM ubuntu:20.04

# Avoid tzdata interactive prompt during apt-get install
ENV DEBIAN_FRONTEND=noninteractive

# System tools, Python 3.9, MySQL 8.0 client, MongoDB 4.4 shell
RUN apt-get update && apt-get install -y \
    software-properties-common \
    git \
    curl \
    gnupg \
    wget \
    mysql-client default-mysql-client \
    python3.9 \
    python3.9-dev \
    python3.9-distutils \
    python3-pip \
    && curl -fsSL https://repo.charm.sh/apt/gpg.key \
        | gpg --dearmor -o /etc/apt/keyrings/charm.gpg \
    && echo "deb [signed-by=/etc/apt/keyrings/charm.gpg] https://repo.charm.sh/apt/ * *" \
        > /etc/apt/sources.list.d/charm.list \
    && wget -qO - https://www.mongodb.org/static/pgp/server-4.4.asc | apt-key add - \
    && echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/4.4 multiverse" | tee /etc/apt/sources.list.d/mongodb-org-4.4.list \
    && apt-get update && apt-get install -y glow mongodb-org-shell \
    && rm -rf /var/lib/apt/lists/*

# Map python3 to python3.9 explicitly if needed
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.9 1 \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3.9 1 \
    && python3 -m pip install --upgrade pip

# matplotlib in headless mode (no GUI window - save figures to files instead)
ENV MPLBACKEND=Agg

WORKDIR /workspace

COPY requirements.txt .
RUN pip3 install --no-cache-dir -r requirements.txt
