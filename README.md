# SupportOps OpenEnv

## Description
This environment simulates real-world customer support workflows where an AI agent classifies, prioritizes, and responds to user tickets.

## Tasks
- Easy: Spam detection
- Medium: Billing issue resolution
- Hard: Complaint handling with escalation

## API
- POST /reset
- POST /step
- GET /tasks
- GET /baseline
- GET /grader

## Run Locally
python -m uvicorn server:app --reload

## Docker
docker build -t openenv .
docker run -p 7860:7860 openenv