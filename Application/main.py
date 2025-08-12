from fastapi import FastAPI
- from application.routes import health, auth, assistance
+ from .routes import health, auth, assistance
app = FastAPI(title="MechMate API", version="1.0")

# Include routes
app.include_router(health.router)
app.include_router(auth.router)
app.include_router(assistance.router)

@app.get("/")
def root():
    return {"message": "Welcome to MechMate API"}
