import asyncio
from pprint import pprint as print
from random import randint

import httpx

# from dataclasses import dataclass
import requests
from pydantic import BaseModel, Extra

BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
MIN_POKEMON_ID = 1
MAX_POKEMON_ID = 700


class Species(BaseModel):
    name: str
    url: str


class Pokemon(BaseModel):
    name: str
    species: Species | None
    # blabla: Optional[int]
    base_experience: int

    class Config:
        extra = Extra.allow


def get_pokemon(id_: int) -> Pokemon:
    url: str = "".join([BASE_URL, str(id_)])
    response: dict = requests.get(url).json()

    return Pokemon(name=response["name"], base_experience=response["base_experience"])


async def get_pokemon_async(id_: int) -> Pokemon:
    # return await asyncio.to_thread(get_pokemon, id_)

    url: str = "".join([BASE_URL, str(id_)])
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return Pokemon(**response.json())


def get_random_id(min_id=MIN_POKEMON_ID, max_id=MAX_POKEMON_ID) -> int:
    return randint(min_id, max_id)


async def main():
    amount = 10
    # pokemons: list[Pokemon] = [get_pokemon(get_random_id()) for _ in range(amount)]
    tasks = [get_pokemon_async(get_random_id()) for _ in range(amount)]
    pokemons = await asyncio.gather(*tasks)

    print(pokemons[0])
    # for pokemon in pokemons:
    # print(pokemon)


if __name__ == "__main__":
    asyncio.run(main())
