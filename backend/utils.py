def normalize_score(score):
    """
    Ensures risk score is between 0-100
    """
    return max(0, min(100, score))

def categorize_risk(score):
    if score < 35:
        return "Safe"
    elif score < 70:
        return "Moderate"
    else:
        return "High-Risk"
