# FastAPI Project

A simple FastAPI application.

## Setup

1. Create virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Linux/Mac
   # or
   .venv\Scripts\activate  # On Windows

2. Install dependency:
   ```bash
   pip install fastapi uvicorn pydantic

## Run
   ```bash
   uvicorn main:app --reload