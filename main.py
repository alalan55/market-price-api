from fastapi import FastAPI
from routes import user, task
# import models.model
from db.config_db import engine

# models.model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)


@app.get("/")
async def root():
    return "Health"
