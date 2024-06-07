# main.py
# Entry point for the application.

from fastapi import FastAPI
from routers import router as api_router
from db import Base, engine

# Create the database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include the routers
app.include_router(api_router, prefix="/api", tags=["api"])

# Run the application with Python command
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
