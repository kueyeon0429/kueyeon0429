import feedparser, time

URL="https://noooey.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=3

markdown_text = """

**Blog~...✍️**  
""" # list of blog posts will be appended here

idx = 0
for feed in enumerate(RSS_FEED['entries']):
    if idx > MAX_POST:
        break
    else:
        feed_category = feed['category']
        if feed_category in ['AI', 'DataEngineering', 'Infra']:
            feed_date = feed['published_parsed']
            markdown_text += f"{time.strftime('%Y.%m.%d', feed_date)} | #{feed_category}) <br/> \n"
            markdown_text += f"### [{feed['title']}]({feed['link']}) <br/> \n"
            idx += 1

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
