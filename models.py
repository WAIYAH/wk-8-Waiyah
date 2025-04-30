from pydantic import BaseModel

class Book(BaseModel):
    Title: str
    Author: str
    ISBN: str
    PublicationYear: int
    AvailableCopies: int