import requests
import pandas as pd
import time
import os

API_KEY = "ee0a79d0"  # My personal API key

movies_list = [
    "The Shawshank Redemption", "The Godfather", "The Dark Knight", "Pulp Fiction",
    "The Lord of the Rings: The Return of the King", "Forrest Gump", "Inception",
    "Fight Club", "The Matrix", "Goodfellas", "Star Wars: Episode IV - A New Hope",
    "The Empire Strikes Back", "The Lord of the Rings: The Fellowship of the Ring",
    "The Lord of the Rings: The Two Towers", "Interstellar", "Se7en",
    "The Silence of the Lambs", "Saving Private Ryan", "Schindler's List",
    "The Green Mile", "Gladiator", "Titanic", "Back to the Future", "The Prestige",
    "Whiplash", "The Departed", "Memento", "Parasite", "The Lion King",
    "A Clockwork Orange", "Alien", "The Revenant", "Mad Max: Fury Road", "Joker",
    "Toy Story", "WALL·E", "The Social Network", "La La Land", "Django Unchained",
    "The Truman Show", "The Grand Budapest Hotel", "Blade Runner 2049",
    "No Country for Old Men", "There Will Be Blood", "Black Swan",
    "The Intouchables", "Coco", "Up", "The Pianist", "Amélie"
]

os.makedirs("../data", exist_ok=True)
save_path = "../data/raw_imdb_movies.csv"

data = []
failed = []

for title in movies_list:
    url = f"http://www.omdbapi.com/?t={requests.utils.quote(title)}&apikey={API_KEY}"
    try:
        resp = requests.get(url, timeout=10)
        j = resp.json()
        if j.get("Response", "False") == "True":
            data.append(j)
        else:
            failed.append({"title": title, "error": j.get("Error", "Unknown")})
    except Exception as e:
        failed.append({"title": title, "error": str(e)})
    time.sleep(0.25)

df = pd.DataFrame(data)
df.to_csv(save_path, index=False)
print(f"Saved {save_path} with {len(df)} rows")

if failed:
    print("\nFAILED MOVIES:")
    for f in failed:
        print(f)
