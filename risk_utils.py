def calculate_risk(predicted_load, capacity=50):
    risk = predicted_load / capacity

    if risk >= 0.8:
        return "HIGH", risk
    elif risk >= 0.6:
        return "MODERATE", risk
    else:
        return "NORMAL", risk


def estimate_waiting_time(predicted_load, capacity=50, dispatch_rate=10):
    if predicted_load <= capacity:
        return 0
    return round((predicted_load - capacity) / dispatch_rate, 2)
