# Application/main.py

from fastapi import FastAPI
from Application.routes import auth, health, assistance

app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(health.router, prefix="/health")
app.include_router(assistance.router, prefix="/assist")

