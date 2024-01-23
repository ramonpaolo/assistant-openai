from pydantic import BaseModel

class BodyMessage(BaseModel):
    message: str

class User(BaseModel):
  name: str