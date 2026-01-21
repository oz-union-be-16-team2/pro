from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# 랜덤 질문 요청
class RandomQuestionRequest(BaseModel):
    category: Optional[str] = Field(
        default=None,
        description="Filter questions by category (optional)"
    )


# 질문 단일 응답
class QuestionResponse(BaseModel):
    id: int
    question_text: str
    category: Optional[str] = None

    class Config:
        from_attributes = True


# 랜덤 질문 응답
class RandomQuestionResponse(BaseModel):
    data: QuestionResponse


# 사용자가 받은 질문 기록
class UserQuestionRecord(BaseModel):
    received_at: datetime
    question: QuestionResponse


# 받은 질문 목록 응답
class UserQuestionHistoryResponse(BaseModel):
    data: List[UserQuestionRecord]
    limit: int
    offset: int
    total: int
