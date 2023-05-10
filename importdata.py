#importing data from CVS file
import pandas as pd

#read_csv
# Step 1: Get the data
df = pd.read_csv('horror_movies.csv', index_col=0)
print(df)

#Third movie details(Smile)
third_movie = df.iloc[2]
print("Details of the third moviee:")
print(third_movie)

#Fifht movie details (Presencias)
result = df.iloc[4]
print("Details of the fifth movie of the DataFrame:")
print(result)

# Creating an smaller dataframe with a subset of all feautures
small_df = df[['title', 'release_date', 'budget', 'revenue', 'runtime']]
print("Smaller DataFrame:")
print(small_df.head())

#Sort Movies based on runtime in descending order
result = small_df.sort_values('runtime', ascending=False)
print("DataFrame sort on Runtime.")
print(result.head())

#Revenue that made more than 2 mil, and spent less than 1 mil
result = small_df[(small_df['revenue'] > 2000000) & (small_df['budget'] <
1000000)]
print("Movies, revenue more than 2 million and spent less than 1 million:")
print(result.head())

#Movies longer than 30min and shorter than 360min
n = 500
small_df = df[['title', 'vote_count','popularity','runtime']]
result = small_df[small_df['vote_count'] >= n]
print("List of movies longer than 30 minutes and shorter than 360 minutes:")
print(result)

#Calculating the number of votes garnered by the 70% movie.
result = df['vote_count'].quantile(0.70)
print(result)