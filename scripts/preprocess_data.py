import pandas as pd
import os

df = pd.read_csv("../data/raw_imdb_movies.csv")

cols_keep = ["Title", "Year", "Rated", "Released", "Runtime", "Genre", "Director",
             "Writer", "Actors", "Plot", "Language", "Country", "Awards", "Poster",
             "Metascore", "imdbRating", "imdbVotes", "Type", "DVD", "BoxOffice", "Production"]

for c in cols_keep:
    if c not in df.columns:
        df[c] = pd.NA

df = df[cols_keep]

df["Year"] = pd.to_numeric(df["Year"], errors="coerce")
df["imdbRating"] = pd.to_numeric(df["imdbRating"], errors="coerce")
df["Metascore"] = pd.to_numeric(df["Metascore"], errors="coerce")
df["imdbVotes"] = df["imdbVotes"].astype(str).str.replace(",", "")
df["imdbVotes"] = pd.to_numeric(df["imdbVotes"], errors="coerce")
df["Runtime"] = df["Runtime"].astype(str).replace("min", "").str.replace(" min", "", regex=False)
df["Runtime"] = pd.to_numeric(df["Runtime"], errors="coerce")
df["BoxOffice"] = df["BoxOffice"].astype(str).str.replace("$", "").str.replace(",", "")
df["BoxOffice"] = pd.to_numeric(df["BoxOffice"], errors="coerce")

numeric_cols = ["Year", "imdbRating", "imdbVotes", "Metascore", "Runtime", "BoxOffice"]
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].median())

df = df.drop_duplicates(subset=["Title","Year"])

df.to_csv("../data/cleaned_imdb_movies.csv", index=False)
print("Saved cleaned_imdb_movies.csv")