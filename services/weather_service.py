import os
import httpx
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

async def fetch_weather(capital: str):

    if not capital:
        return None

    url = f"http://api.openweathermap.org/data/2.5/weather?q={capital}&appid={API_KEY}&units=metric"

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code != 200:
        return None

    data = response.json()

    return {
        "temperature": data["main"]["temp"]
    }