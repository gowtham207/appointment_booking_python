from pydantic import BaseModel


class ResponseModel(BaseModel):
    data: dict | list | None = None
    message: str | None = None
    error: str | None = None
