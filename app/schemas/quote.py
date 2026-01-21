from pydantic import BaseModel, Field
from typing import Optional, List


class QuoteResponse(BaseModel):
    id: int
    content: str
    author: Optional[str] = None

    class Config:
        from_attributes = True


class RandomQuoteQuery(BaseModel):
    limit: int = Field(default=1, ge=1, le=10)
    author: Optional[str] = None


class RandomQuoteResponse(BaseModel):
    data: List[QuoteResponse]
