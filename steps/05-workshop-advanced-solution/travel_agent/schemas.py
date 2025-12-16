from pydantic import BaseModel, Field


class TravelRequest(BaseModel):
    destination: str = Field(description="La ville ou pays de destination")
    budget: float = Field(description="Budget en euros", ge=0)
    days: int = Field(description="Nombre de jours", ge=1)
    interests: list[str] = Field(
        description="Liste des centres d'intérêt (culture, nature, gastronomie, etc.)"
    )


class TravelResponse(BaseModel):
    destination: str
    daily_budget: float
    activities: list[str]
    accommodation_type: str
    estimated_total_cost: float
