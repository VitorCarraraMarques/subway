from pydantic import BaseModel

class BorderModel(BaseModel):
    source: str
    dest: str 