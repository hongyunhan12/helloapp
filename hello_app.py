"""
Minimal FastAPI application with Hello World endpoint
"""
from fastapi import FastAPI

app = FastAPI(title="Hello World API")


@app.get("/hello/{input}")
async def hello(input: str):
    """
    Returns a greeting message with the input parameter
    """
    return {"message": f"Hello, World {input}"}

