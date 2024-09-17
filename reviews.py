import pandas as pd

reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', index_col=0)

reviews_data = reviews[["country", "points"]]
summary = reviews_data.groupby("country").agg(
    Count=("points", "size"),
    Points=("points", "mean")

).reset_index()

summary["Points"] = summary["Points"].round(1)

summary = summary.sort_values(by="Count", ascending=False)

summary.to_csv('data/reviews-per-country.csv')

print('summary')
