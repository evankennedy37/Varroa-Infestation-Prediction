@echo off
cd /d "%~dp0"

echo Building Docker image...
docker compose -f pipeline.yml build --no-cache

echo Running container...
docker compose -f pipeline.yml up --remove-orphans

pause