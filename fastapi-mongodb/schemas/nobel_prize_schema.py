from models.LaureatesModel import Laureates
from models.NobelPrizeModel import NobelPrize
import random


def nobel_prize_serializer(nobel_prize) -> dict:
    try:
        return {
            'id': str(nobel_prize['_id']),
            'year': str(nobel_prize['year']),
            'category': str(nobel_prize['category']),
            'laureates': list(nobel_prize_laureates_serializer(nobel_prize['laureates']))
        }
    except Exception as e:
        print(e.__cause__)


def nobel_prize_laureate_serializer(laureate) -> dict:
    try:
        return {
            'id': str(laureate['id']),
            'firstname': str(laureate['firstname']),
            'surname': str(laureate['surname']),
            'motivation': str(laureate['motivation']),
            'share': str(laureate['share'])
        }
    except Exception as e:
        print(e.__cause__)


def nobel_prize_laureates_serializer(laureates) -> list:
    try:
        return [nobel_prize_laureate_serializer(laureate) for laureate in laureates]
    except Exception as e:
        print(e.__cause__)


def nobel_prizes_serializer(nobel_prizes) -> list:
    try:
        return [nobel_prize_serializer(nobel_prize) for nobel_prize in nobel_prizes]
    except Exception as e:
        print(e.__cause__)


def serialize_payload(payload: NobelPrize) -> dict:
    try:
        return {
            'year': str(payload.year),
            'category': str(payload.category),
            'laureates': serialize_payload_laureates_arrays(payload.laureates)
        }
    except Exception as e:
        print(e.__cause__)


def serialize_payload_laureates_arrays(laureates) -> list:
    return [serialize_payload_laureates_object(laureate) for laureate in laureates]


def serialize_payload_laureates_object(laureate: Laureates) -> dict:
    return {
        'id': str(random.randint(0, 99999999)),
        'firstname': str(laureate.firstname),
        'surname': str(laureate.surname),
        'motivation': str(laureate.motivation),
        'share': str(laureate.share)
    }
