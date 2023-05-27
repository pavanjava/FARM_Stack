from fastapi import APIRouter
from models.NobelPrizeModel import NobelPrize
from schemas.nobel_prize_schema import nobel_prizes_serializer, serialize_payload
from bson import ObjectId
from config.db import collection

nobel_prize_routes = APIRouter()


@nobel_prize_routes.get("/nobel-prize")
async def find_all_nobel_prize(category: str | None = None, year: str | None = None):
    query = {}
    if category is not None:
        query['category'] = category
    if year is not None:
        query['year'] = year
    data: list[NobelPrize] = nobel_prizes_serializer(collection.find(query))

    return {"status": "OK", "total": len(data), "data": data}


@nobel_prize_routes.get("/nobel-prize/{id}")
async def find_nobel_prize_by_id(_id: str):
    data: list[NobelPrize] = nobel_prizes_serializer(collection.find({'_id': ObjectId(_id)}))
    return {"status": "OK", "data": data}


@nobel_prize_routes.post("/nobel-prize")
async def save_nobel_prize(payload: NobelPrize):
    payload = serialize_payload(payload)
    response = collection.insert_one(dict(payload))
    nobel_prize = nobel_prizes_serializer(collection.find({"_id": response.inserted_id}))
    return {"status": "Ok", "acknowledged": response.acknowledged, "data": nobel_prize}
