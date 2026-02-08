from pydantic import BaseModel


class LocationModel(BaseModel):
    name: str
    address: str
    city: str
    state: str
    country: str
    postal_code: str
