from fastapi import FastAPI
from routes.nobel_prize_routes import nobel_prize_routes
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(nobel_prize_routes)

@app.get("/health")
async def root():
    return {"health": "OK"}

