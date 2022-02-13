import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

res = requests.get(URL)
soup = BeautifulSoup(res.text, "html.parser")
movie_list = []
for title in soup.find_all(name="h3", class_="title"):
    movie_list.insert(0, title.text)

with open('movie_list.txt', 'w', encoding='utf-8') as file :
    for movie in movie_list:
        file.write(movie + '\n')
