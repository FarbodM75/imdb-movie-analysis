import pandas as pd

df = pd.read_csv("../data/cleaned_imdb_movies.csv")

print("\nDESCRIPTIVE STATS:")
print(df.describe())

print("\nTOP 10 MOVIES:")
print(df.sort_values(["imdbRating","imdbVotes"], ascending=[False,False]).head(10))

print("\nCORRELATIONS:")
print(df.corr(numeric_only=True))

df["Decade"] = (df["Year"] // 10) * 10
print("\nAVG RATING BY DECADE:")
print(df.groupby("Decade")["imdbRating"].mean())
