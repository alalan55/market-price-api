from fastapi import FastAPI
from routes import user, task
from models import model
from db.config_db import engine

model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)


@app.get("/")
async def root():
    return "Health"
