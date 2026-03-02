import httpx
from fastapi import HTTPException

async def fetch_country_profile(country: str):

    url = f"https://restcountries.com/v3.1/name/{country}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        raise HTTPException(status_code=404, detail=f"{country} not found")

    data = response.json()[0]

    return {
        "country": country,
        "capital": data.get("capital", [None])[0],
        "population": data.get("population"),
        "country_code": data.get("cca2")
    }