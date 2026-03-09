from pydantic import BaseModel

class PostRequest(BaseModel):
    Title: str
    Description: str

class PostResponse(BaseModel):
    Title: str
    Description: str