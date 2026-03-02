import httpx

LIFE_EXPECTANCY = "SP.DYN.LE00.IN"
HEALTH_EXPENDITURE = "SH.XPD.CHEX.GD.ZS"

async def fetch_worldbank_health_data(country_code: str):

    if not country_code:
        return {"life_expectancy": None, "health_expenditure": None}

    base_url = "https://api.worldbank.org/v2/country"

    life_url = f"{base_url}/{country_code}/indicator/{LIFE_EXPECTANCY}?format=json"
    health_url = f"{base_url}/{country_code}/indicator/{HEALTH_EXPENDITURE}?format=json"

    async with httpx.AsyncClient() as client:
        life_response = await client.get(life_url)
        health_response = await client.get(health_url)

    life_value = None
    health_value = None

    try:
        life_json = life_response.json()
        health_json = health_response.json()

        for item in life_json[1]:
            if item["value"] is not None:
                life_value = item["value"]
                break

        for item in health_json[1]:
            if item["value"] is not None:
                health_value = item["value"]
                break

    except:
        pass

    return {
        "life_expectancy": life_value,
        "health_expenditure": health_value
    }