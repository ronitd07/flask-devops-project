# Flask DevOps CI/CD Project

## Project Overview
This project demonstrates an end-to-end DevOps workflow for a Python Flask application.

## Tools Used
- Python Flask
- Git and GitHub
- Docker
- GitHub Actions
- Docker Hub
- AWS EC2
- Prometheus
- Grafana

## Architecture
Developer → GitHub → GitHub Actions → Docker Hub → AWS EC2 → Prometheus/Grafana

## Features
- Flask web application
- Dockerized deployment
- Automated Docker image build and push
- Deployment on AWS EC2
- Health check endpoint
- Prometheus metrics endpoint
- Grafana monitoring dashboard

## Application Endpoints
- `/`
- `/health`
- `/metrics`

## CI/CD Pipeline
The pipeline is triggered when code is pushed to the main branch.
It builds a Docker image and pushes it to Docker Hub.