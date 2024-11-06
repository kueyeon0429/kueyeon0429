import feedparser
import time
from typing import Dict
import sys

def parse_rss_feed(url: str) -> dict:
    feed = feedparser.parse(url)
    if feed.bozo:  # RSS 파싱 에러 체크
        print(f"RSS 파싱 에러: {feed.bozo_exception}")
        sys.exit(1)
    return feed

def generate_markdown(feed: dict, max_posts: int = 6) -> str:
    markdown_text = """
<a href="https://github.com/devxb/gitanimals">
  <img src="https://render.gitanimals.org/lines/{noooey}?pet-id=582855096513082436" width="1000" height="120"/>
</a>
  
Blog____✍️  
---
"""
    category: Dict[str, int] = {
        'AI': 0, 
        'Data Engineering': 0, 
        'Infra': 0, 
        'Algorithm': 0, 
        'CS': 0
    }
    
    post_count = 0
    for entry in feed.get('entries', []):
        if post_count >= max_posts:
            break
            
        feed_category = entry.get('category')
        if not feed_category:
            continue
            
        if feed_category in category and category[feed_category] < 3:
            try:
                feed_date = entry.get('published_parsed')
                if not feed_date:
                    continue
                    
                markdown_text += f"[{entry.get('title', 'No Title')}]({entry.get('link', '#')}), {time.strftime('%Y.%m.%d', feed_date)} <br/> \n"
                category[feed_category] += 1
                post_count += 1
            except (KeyError, AttributeError) as e:
                print(f"포스트 처리 중 에러 발생: {e}")
                continue

    # 나머지 고정 콘텐츠 추가
    markdown_text += "\n"
    markdown_text += """
Summary  
---
**2023.08 ~ 2023.09** | `공모전`  제11회 2023 빅콘테스트, 대상  
**2023.05 ~ 2023.08** | `공모전`  2023 오픈인프라개발경진대회, 금상  
**2023.04 ~ 2023.08** | `연 구`  산학협력 학부연구,  패션상품도메인 고속 유사이미지 검색 알고리즘 연구  
**2023.02 ~ 2023.02** | `공모전`  제1회 2023년 지역 치안 안전 데이터 분석 공모전, 최우수상  
**2022.03 ~ 2022.06** | `인 턴`  Front-end Developer in CONCAT Inc.  
**2022.01 ~ 2023.01** | `동아리` 국내 최초 빅데이터 연합동아리 BOAZ, 18기 분석 부문 대표
"""
    markdown_text += "\n"
    markdown_text += "---\n"
    markdown_text += "qkrrbdus1859@gmail.com"
    
    return markdown_text

def main():
    URL = "https://noooey.tistory.com/rss"
    
    try:
        feed = parse_rss_feed(URL)
        markdown_content = generate_markdown(feed)
        
        with open("README.md", mode="w", encoding="utf-8") as f:
            f.write(markdown_content)
            
    except Exception as e:
        print(f"에러 발생: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
