from fastapi import FastAPI
from routes import user, task
from db.config_db import engine
from db.models import user_model, task_model

# user_model.Base.metadata.create_all(bind=engine)
# task_model.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(task.router)


@app.get("/")
async def root():
    return "Health"
