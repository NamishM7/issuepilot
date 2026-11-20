from fastapi import FastAPI
from app.api.issues import router as issues_router

# fastapi application
app = FastAPI(title="IssuePilot", 
              description="AI-Powered Github issue Triage and Management Assistant",
              version="1.0.0")

app.include_router(issues_router, prefix="/api/v1")

# root endpoint
@app.get("/")
def root():
    return {
        "message" : "Welcome to IssuePilot!",
        "status" : "running"
    }

# health check endpoint
@app.get("/health")
def health_check():
    return {
        "status":"healthy",
        "application" : "IssuePilot" 
    }