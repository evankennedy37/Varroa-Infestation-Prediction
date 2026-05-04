@echo off
cd /d "%~dp0"

echo Building Docker image...
docker compose -f predict.yml build --no-cache

echo Running container...
docker compose -f predict.yml up --remove-orphans

pause