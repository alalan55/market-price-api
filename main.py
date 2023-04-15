from fastapi import FastAPI
from database import engine
from routes import auth, user
import models

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(user.router)


@app.get("/health")
async def health():
    return {"message": "ok"}
