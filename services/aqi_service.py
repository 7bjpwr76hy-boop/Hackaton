import os
import httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("AQICN_API_KEY")

async def fetch_aqi(capital: str):

    if not capital:
        return None

    url = f"https://api.waqi.info/feed/{capital}/?token={API_KEY}"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    if data.get("status") != "ok":
        return None

    return {
        "aqi": data["data"]["aqi"]
    }