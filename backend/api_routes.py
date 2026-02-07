from fastapi import APIRouter
from models import get_risk_score

router = APIRouter()

@router.get("/risk")
def get_risk(lat: float, lon: float, time_of_day: str):
    """
    Returns risk score and category for a given location and time.
    """
    risk_score, risk_category = get_risk_score(lat, lon, time_of_day)
    return {"risk_score": risk_score, "risk_category": risk_category}
