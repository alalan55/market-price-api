from fastapi import FastAPI
from database import engine
from routes import auth
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)


@app.get("/health")
async def health():
    return {"message": "ok"}
