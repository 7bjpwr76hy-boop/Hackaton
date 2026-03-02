import time
import asyncio
from fastapi import FastAPI, HTTPException
from services.country_service import fetch_country_profile
from services.weather_service import fetch_weather
from services.aqi_service import fetch_aqi
from services.worldbank_service import fetch_worldbank_health_data
from scoring.score_engine import compute_scores
from scoring.weighting import get_weights
from fastapi.middleware.cors import CORSMiddleware


from pydantic import BaseModel
from typing import List

class AnalyzeRequest(BaseModel):
    countries: List[str]
    risk_tolerance: str
    duration: str
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For development
    allow_credentials=True,
    allow_methods=["*"],  # THIS FIXES 405
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"status": "Global Relocation Intelligence Engine Running"}


@app.post("/api/analyze")
async def analyze(request: AnalyzeRequest):

    if len(request.countries) < 1:
        raise HTTPException(status_code=400, detail="At least one country required")

    start_time = time.time()
    weights = get_weights(request.risk_tolerance, request.duration)

    results = []

    for country in request.countries:

        try:
            profile = await fetch_country_profile(country)

            capital = profile["capital"]
            country_code = profile["country_code"]

            weather, aqi, health_data = await asyncio.gather(
                fetch_weather(capital),
                fetch_aqi(capital),
                fetch_worldbank_health_data(country_code)
            )

            scores = compute_scores(profile, weather, aqi, health_data, weights)

            results.append(scores)

        except Exception as e:
            results.append({
                "country": country,
                "error": str(e)
            })

    results.sort(key=lambda x: x.get("overall_score", 0), reverse=True)

    return {
        "processing_time_seconds": round(time.time() - start_time, 2),
        "weights_used": weights,
        "ranking": results
    }

