def get_weights(risk_tolerance, duration):

    if risk_tolerance == "Low":
        risk = 0.5
    elif risk_tolerance == "High":
        risk = 0.2
    else:
        risk = 0.35

    if duration == "Long-term":
        health = 0.4
        environment = 0.2
    else:
        health = 0.2
        environment = 0.4

    return {
        "risk": risk,
        "health": health,
        "environment": environment
    }