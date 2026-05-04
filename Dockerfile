#For the Docker Compose implementation of the pipeline
FROM python:3.11-slim AS pipeline

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Sparse checkout — only pull notebooks/ and Requirements.txt
RUN git clone --no-checkout https://github.com/evankennedy37/Varroa-Infestation-Prediction . && \
    git sparse-checkout init --cone && \
    git sparse-checkout set pipeline/ Requirements.txt && \
    git checkout main

# Install repo dependencies
RUN pip install --no-cache-dir -r Requirements.txt



#For the Docker Compose implementation of the predictor-only
FROM python:3.11-slim AS predict

WORKDIR /app

RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Sparse checkout — only pull predictions notebook, its easy-run script and Requirements.txt
RUN git clone --no-checkout https://github.com/evankennedy37/Varroa-Infestation-Prediction . && \
    git sparse-checkout init --no-cone && \
    git sparse-checkout set "pipeline/Varroa Infestation Prediction - Predictor.ipynb" utilities/predict.py Requirements.txt && \
    git checkout main

# Install repo dependencies
RUN pip install --no-cache-dir -r Requirements.txt



#For distribution [Retired Functionality]
#FROM python:3.11-slim AS full

#WORKDIR /app

#RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# Full clone of the entire repository
#RUN git clone https://github.com/evankennedy37/Varroa-Infestation-Prediction .

# Install all dependencies
#RUN pip install --no-cache-dir -r Requirements.txt