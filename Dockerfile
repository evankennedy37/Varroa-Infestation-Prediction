FROM python:3.11-slim AS pipeline

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Sparse checkout — only pull notebooks/ and requirements.txt
RUN git clone --no-checkout https://github.com/evankennedy37/Varroa-Infestation-Prediction . && \
    git sparse-checkout init --cone && \
    git sparse-checkout set pipeline/ requirements.txt && \
    git checkout main

# Install repo dependencies
RUN pip install --no-cache-dir -r Requirements.txt