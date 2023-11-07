import feedparser, time

URL="https://noooey.tistory.com/rss"
RSS_FEED = feedparser.parse(URL)
MAX_POST=3

markdown_text = """

Blog____✍️  
---

""" # list of blog posts will be appended here

category = {'AI': 0, 'DataEngineering':0, 'Infra':0, 'Algorithm':0}

idx = 0
for feed in RSS_FEED['entries']:
    if idx > MAX_POST:
        break
    else:
        feed_category = feed['category']
        if feed_category in category.keys() and category[feed_category] == 0:
            feed_date = feed['published_parsed']
            markdown_text += f"**[{feed['title']}]({feed['link']})**, {time.strftime('%Y.%m.%d', feed_date)} <br/> \n"
            category[feed_category] = 1 # checked!
            idx += 1

markdown_text += "\n--- \n"
markdown_text += "20203065@kookmin.ac.kr"

f = open("README.md",mode="w", encoding="utf-8")
f.write(markdown_text)
f.close()
