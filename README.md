# Hello App - Minimal FastAPI Application

A minimal FastAPI web application with a simple Hello World endpoint.

## Features

- FastAPI web framework
- Single endpoint: `/hello/{input}`
- Returns JSON: `{"message": "Hello, World <input>"}`
- Auto-reload in development mode

## Installation

```bash
pip install fastapi uvicorn
```

## Running the Application

### Development Mode (with auto-reload)

```bash
py -m uvicorn hello_app:app --reload --host 0.0.0.0 --port 8000
```

Or on Linux/Mac:

```bash
uvicorn hello_app:app --reload --host 0.0.0.0 --port 8000
```

## Usage

Once the server is running, you can access:

- **API Endpoint**: `http://localhost:8000/hello/{input}`
  - Example: `http://localhost:8000/hello/World` returns `{"message": "Hello, World World"}`
  
- **Interactive API Documentation**: `http://localhost:8000/docs`
- **Alternative API Documentation**: `http://localhost:8000/redoc`

## Example

```bash
curl http://localhost:8000/hello/Test
```

Response:
```json
{"message": "Hello, World Test"}
```

## Project Structure

```
helloapp/
├── hello_app.py      # Main FastAPI application
└── README.md         # This file
```

