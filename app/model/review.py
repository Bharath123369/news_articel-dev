from pydantic import BaseModel, conint

class Review(BaseModel):
    reviewer: str
    comment: str
    rating: conint(ge=1, le=5)
