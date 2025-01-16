# built in
from typing import List
from datetime import datetime

# internal
from src.api.models import Query, Response
from src.api.client import send_message

# external
from fastapi import FastAPI, Depends

def setup_routes(app: FastAPI):
    @app.post("/send_message")
    async def send_message(query: Query) -> Response:
        response = send_message(query)
        return response