from pydantic import BaseModel

class Post(BaseModel):
    Title: str
    Description: str