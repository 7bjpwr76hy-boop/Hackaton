from scoring.normalization import min_max_normalize, reverse_normalize

def compute_scores(profile, weather, aqi, health_data, weights):

    temp = weather["temperature"] if weather else None
    aqi_value = aqi["aqi"] if aqi else None

    life_expectancy = health_data.get("life_expectancy")
    health_expenditure = health_data.get("health_expenditure")

    # Travel Risk Score
    risk_score = (
        reverse_normalize(abs(temp - 22), 0, 25) * 0.4 +
        reverse_normalize(aqi_value, 0, 300) * 0.6
    )

    # Health Score (World Bank data)
    life_score = min_max_normalize(life_expectancy, 50, 85)
    health_exp_score = min_max_normalize(health_expenditure, 2, 15)

    health_score = (life_score * 0.6) + (health_exp_score * 0.4)

    # Environmental Stability
    environment_score = reverse_normalize(aqi_value, 0, 300)

    overall_score = (
        risk_score * weights["risk"] +
        health_score * weights["health"] +
        environment_score * weights["environment"]
    )

    # Explainability
    reasoning = []

    if aqi_value and aqi_value > 150:
        reasoning.append("High air pollution lowered environmental score")

    if life_expectancy and life_expectancy > 80:
        reasoning.append("Strong life expectancy improved health score")

    if not reasoning:
        reasoning.append("Balanced overall performance across indicators")

    return {
        "country": profile["country"],
        "life_expectancy": life_expectancy,
        "health_expenditure": health_expenditure,
        "travel_risk_score": round(risk_score, 2),
        "health_score": round(health_score, 2),
        "environment_score": round(environment_score, 2),
        "overall_score": round(overall_score, 2),
        "reasoning": reasoning
    }