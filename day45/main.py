from bs4 import BeautifulSoup
import requests

res = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(res.text, "html.parser")

article_tags = soup.find_all(name="a", class_="titlelink")
article_texts = []
article_links = []

for tag in article_tags:
    article_txt = tag.getText()
    article_texts.append(article_txt)
    article_link = tag.get("href")
    article_links.append(article_link)

article_upvotes = [int(score.getText().split(" ")[0]) for score in soup.find_all(name="span", class_="score")]

max_num = max(article_upvotes)
max_index = article_upvotes.index(max_num)

print(article_texts[max_index])
print(article_links[max_index])
