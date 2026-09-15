# Production Cloud Platform

A production-style cloud-native platform built to demonstrate modern DevOps and Platform Engineering practices.

## Current Phase

Day 01 focuses on:

- Production-ready Flask API
- Automated tests with Pytest
- Gunicorn production server
- Docker containerization
- Non-root container execution
- Docker health checks
- Environment-based configuration
- Container troubleshooting

## Application Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Application information |
| `/health` | Health check |
| `/ready` | Readiness check |
| `/info` | Runtime information |

## Technology Stack

- Python
- Flask
- Gunicorn
- Docker
- Pytest

## Local Setup

```bash
git clone <repository-url>
cd production-cloud-platform
