import feedparser, time

URL="https://noooey.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=5

markdown_text = """
<a href="https://github.com/devxb/gitanimals">
  <img src="https://render.gitanimals.org/lines/{noooey}?pet-id=1" width="1000" height="120"/>
</a>

Blog____✍️  
---

"""

category = {'AI': 0, 'Data Engineering':0, 'Infra':0, 'Algorithm':0, 'CS':0}

idx = 0
for feed in RSS_FEED['entries']:
    if idx >= MAX_POST:
        break
    else:
        feed_category = feed['category']
        if (feed_category in category.keys()) and (category[feed_category] < 2):
            feed_date = feed['published_parsed']
            markdown_text += f"[{feed['title']}]({feed['link']}), {time.strftime('%Y.%m.%d', feed_date)} <br/> \n"
            category[feed_category] += 1 # count up!
            idx += 1

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
markdown_text += "> 20203065@kookmin.ac.kr"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
