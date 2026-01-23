import random
from datetime import datetime
from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import BaseModel

from app.models import Question, UserQuestion  # app.models/__init__.py에 export 돼있다는 가정
from app.dependencies.auth import get_current_user  # ✅ 너네 실제 위치에 맞게 여기만 바꿔


router = APIRouter(prefix="/questions", tags=["Questions"])


# ----------------------------
# Schemas (필요 최소만 여기서 선언)
# ----------------------------
class RandomQuestionRequest(BaseModel):
    category: Optional[str] = None


class QuestionOut(BaseModel):
    id: int
    question_text: str
    category: Optional[str] = None


class RandomQuestionResponse(BaseModel):
    data: QuestionOut


class UserQuestionHistoryItem(BaseModel):
    id: int
    served_at: datetime
    question: QuestionOut


class UserQuestionHistoryResponse(BaseModel):
    data: List[UserQuestionHistoryItem]
    limit: int
    offset: int
    total: int


# ----------------------------
# Endpoints
# ----------------------------
@router.post("/random", response_model=RandomQuestionResponse)
async def get_random_question(
    payload: RandomQuestionRequest,
    current_user=Depends(get_current_user),
):
    """
    POST /api/v1/questions/random

    - questions 테이블에서 is_active=True 랜덤 1개 선택
    - category 있으면 category 필터
    - ✅ 이미 받은 질문은 제외 (중복 방지)
    - user_questions에 기록 저장
    - 질문 반환
    """
    qs = Question.filter(is_active=True)

    if payload.category:
        qs = qs.filter(category=payload.category)


    total = await qs.count()
    if total == 0:
        raise HTTPException(status_code=404, detail="No more questions available")

    idx = random.randrange(total)
    q = await qs.offset(idx).first()
    if q is None:
        raise HTTPException(status_code=404, detail="No more questions available")

    # 받은 기록 저장
    await UserQuestion.create(user_id=current_user.id, question_id=q.id)

    return {
        "data": {
            "id": q.id,
            "question_text": q.question_text,
            "category": q.category,
        }
    }


@router.get("/me/history", response_model=UserQuestionHistoryResponse)
async def get_my_question_history(
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    current_user=Depends(get_current_user),
):
    """
    GET /api/v1/questions/me/history?limit=20&offset=0

    - user_questions에서 내 기록 조회 (최신순)
    - questions join 해서 질문 내용 포함
    - limit/offset 페이징
    """
    base = UserQuestion.filter(user_id=current_user.id)

    total = await base.count()

    rows = (
        await base.order_by("-created_at")
        .offset(offset)
        .limit(limit)
        .prefetch_related("question")
    )

    data = []
    for row in rows:
        # row.question 은 FK로 연결된 Question 객체
        data.append(
            {
                "id": row.id,
                "served_at": row.created_at,
                "question": {
                    "id": row.question.id,
                    "question_text": row.question.question_text,
                    "category": row.question.category,
                },
            }
        )

    return {
        "data": data,
        "limit": limit,
        "offset": offset,
        "total": total,
    }
