import pandas as pd
import matplotlib.pyplot as plt
import os

df = pd.read_csv("../data/cleaned_imdb_movies.csv")

os.makedirs("../data/plots", exist_ok=True)

plt.hist(df["imdbRating"], bins=10)
plt.title("Distribution of IMDb Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.savefig("../data/plots/ratings_hist.png")
plt.close()

plt.scatter(df["imdbVotes"], df["imdbRating"])
plt.xscale("log")
plt.title("Votes vs Rating")
plt.xlabel("Votes (log)")
plt.ylabel("Rating")
plt.savefig("../data/plots/votes_vs_rating.png")
plt.close()

top10 = df.sort_values(["imdbRating","imdbVotes"], ascending=[False,False]).head(10)
plt.barh(top10["Title"], top10["imdbRating"])
plt.title("Top 10 Movies by Rating")
plt.xlabel("Rating")
plt.savefig("../data/plots/top10_ratings.png")
plt.close()

print("Saved plots")
