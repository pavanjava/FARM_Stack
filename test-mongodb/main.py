from fastapi import FastAPI
from routes.nobel_prize_routes import nobel_prize_routes


app = FastAPI()

app.include_router(nobel_prize_routes)

@app.get("/health")
async def root():
    return {"health": "OK"}

