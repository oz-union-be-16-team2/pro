# app/api/v1/quote.py
from fastapi import APIRouter, HTTPException, Query

from app.schemas.quote import RandomQuoteResponse, QuoteResponse
from app.services.quote_service import QuoteService

router = APIRouter(prefix="/quotes", tags=["Quotes"])
service = QuoteService()


@router.post("/scrape")
async def scrape_quotes_to_db(pages: int = Query(1, ge=1, le=50)):
    """
    POST /api/v1/quotes/scrape?pages=1
    - saramro.com/quotes 스크래핑 후 DB 저장
    """
    try:
        inserted, skipped = await service.scrape_and_save(pages=pages)
        return {"inserted": inserted, "skipped": skipped}
    except Exception as e:
        # 여기서 e 메시지로 원인 확인 가능
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/random", response_model=RandomQuoteResponse)
async def random_quotes(
    limit: int = Query(1, ge=1, le=10),
    author: str | None = None,
):
    """
    GET /api/v1/quotes/random?limit=1&author=...
    - DB에서 랜덤 조회
    """
    data = await service.get_random(limit=limit, author=author)
    return {"data": [QuoteResponse.model_validate(x) for x in data]}