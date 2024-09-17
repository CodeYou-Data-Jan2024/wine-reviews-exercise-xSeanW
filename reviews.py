import pandas as pd
reviews = pd.read_csv('data/winemag-data-130k-v2.csv.zip', index_col=0)
reviews_data = reviews[["country", "points"]]
print(reviews_data)
