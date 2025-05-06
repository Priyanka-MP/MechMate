from fastapi import FastAPI
from Application.routes import health  # <- This matters!

app = FastAPI(title="MechMate Roadside Assistance App")

app.include_router(health.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to MechMate API"}
