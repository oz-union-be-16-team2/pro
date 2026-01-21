# app/services/quote_service.py
from __future__ import annotations

import random
from typing import Optional, List, Tuple

from tortoise.transactions import in_transaction

from app.models.quote import Quote
from app.scraping.quote_scraper import scrape_quotes


class QuoteService:
    async def scrape_and_save(self, pages: int = 1) -> Tuple[int, int]:
        """
        pages 만큼 스크래핑 → DB 저장
        return (inserted, skipped)
        """
        items = scrape_quotes(pages)

        inserted = 0
        skipped = 0

        async with in_transaction():
            for it in items:
                content = (it.get("content") or "").strip()
                author = (it.get("author") or None)

                if not content:
                    skipped += 1
                    continue

                # 중복 방지: content+author 동일하면 skip
                exists = await Quote.filter(content=content, author=author).exists()
                if exists:
                    skipped += 1
                    continue

                await Quote.create(content=content, author=author, is_active=True)
                inserted += 1

        return inserted, skipped

    async def get_random(self, limit: int = 1, author: Optional[str] = None) -> List[Quote]:
        qs = Quote.filter(is_active=True)
        if author:
            qs = qs.filter(author=author)

        total = await qs.count()
        if total == 0:
            return []

        take = min(limit, total)

        # 랜덤 여러 개 뽑기(단순 버전)
        picked = []
        used = set()
        while len(picked) < take:
            idx = random.randrange(total)
            if idx in used:
                continue
            used.add(idx)
            q = await qs.offset(idx).first()
            if q:
                picked.append(q)

        return picked