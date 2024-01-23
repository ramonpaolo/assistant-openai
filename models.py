from pydantic import BaseModel

class BodyMessage(BaseModel):
    message: str