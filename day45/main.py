from bs4 import BeautifulSoup

with open("website.html", encoding="utf-8") as html:
    contents = html.read()

soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

print(soup.find_all(name="a"))
