from fastapi import FastAPI
from app.routes import health

app = FastAPI(title="MechMate Roadside Assistance App")

# Include routes
app.include_router(health.router)

# Root route (optional)
@app.get("/")
def read_root():
    return {"message": "Welcome to MechMate API"}
