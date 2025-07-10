import uvicorn
from fastapi import FastAPI
from app.database import Base, engine
from app.routers import users, onboarding

# create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Onboarding Service")

app.include_router(users.router)
app.include_router(onboarding.router)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8800, reload=True)
