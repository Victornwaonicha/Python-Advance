import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.6 Safari/605.1.15",
    "Accept-Language": "en-US,en;q=0.9",
}

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL, headers=headers)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_strongs = soup.find_all(name="strong")

movie_titles = []

# movies_titles = [movie.getText() for movie in all_movies]

for tag in all_strongs:
    text = tag.get_text(strip=True)
    if text[0].isdigit():      # keeps only titles like "1) The Lord …"
        movie_titles.append(text)

# Reverse the list (100 → 1)
movie_titles = list(reversed(movie_titles))

# Write **full titles**, one per line
with open("movies.txt", mode="w") as file:
    for movie in movie_titles:
        file.write(f"{movie}\n")











