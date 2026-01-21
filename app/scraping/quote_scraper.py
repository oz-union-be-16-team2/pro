# app/scraping/quote_scraper.py
from __future__ import annotations

import re
from typing import List, Dict, Optional

import requests
from bs4 import BeautifulSoup


def _clean_text(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()


def scrape_quotes(pages: int = 1) -> List[Dict[str, Optional[str]]]:
    """
    saramro.com/quotes?page=N 에서 명언(content) / 저자(author) 추출
    반환: [{"content": "...", "author": "..."}]
    """
    results: List[Dict[str, Optional[str]]] = []

    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome Safari"
    }

    for page in range(1, pages + 1):
        url = "https://saramro.com/quotes" if page == 1 else f"https://saramro.com/quotes?page={page}"
        r = requests.get(url, headers=headers, timeout=15)
        r.raise_for_status()

        soup = BeautifulSoup(r.text, "html.parser")

        # 페이지에 "15160 ... 명언 ... 인생이란 ... - 필립 ..." 이런 식으로 텍스트가 들어있음  [oai_citation:1‡saramro.com](https://saramro.com/quotes?page=2)
        # 일단 컨텐츠 영역 텍스트를 라인 단위로 모아 정리 후 파싱
        main = soup.get_text("\n")
        lines = [_clean_text(x) for x in main.split("\n")]
        lines = [x for x in lines if x]

        # 패턴: (quote content) 다음 줄에 "- author" 형태가 많음  [oai_citation:2‡saramro.com](https://saramro.com/quotes?page=2)
        # 너무 공격적으로 잡으면 노이즈가 섞일 수 있어서, " - "로 시작하는 라인만 저자로 인식
        i = 0
        while i < len(lines) - 1:
            content = lines[i]
            nxt = lines[i + 1]

            # 저자 라인이 "- " 로 시작하는 케이스
            if nxt.startswith("- "):
                author = nxt[2:].strip() or None

                # 컨텐츠가 너무 짧거나, 메뉴/기타 텍스트면 제외 (대충 안전장치)
                if len(content) >= 8 and "페이지" not in content and "명언 목록" not in content:
                    results.append({"content": content, "author": author})
                i += 2
                continue

            i += 1

    # 중복 제거 (content+author)
    uniq = {}
    for item in results:
        key = (item["content"], item["author"])
        uniq[key] = item
    return list(uniq.values())