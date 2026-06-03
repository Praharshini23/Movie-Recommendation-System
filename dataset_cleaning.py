
df = pd.read_csv(" ")

print(df)

df.describe()

movies_df = df[df['type'] == 'Movie'].copy()
movies_df = df[df['type'] == 'Movie']
movies_df.head()

movies=movies_df.dropna()
movies_df = movies_df.reset_index(drop=True)

movies_df = movies_df[
    ['title', 'director', 'cast',
     'country', 'release_year', 'listed_in']
]

movies_df['director'] = movies_df['director'].fillna('Unknown')
movies_df['cast'] = movies_df['cast'].fillna('Unknown')
movies_df['country'] = movies_df['country'].fillna('Unknown')

movies_df.head()

movies_df['listed_in'] = movies_df['listed_in'].apply(
    lambda x: x.split(', ')
)

transactions = movies_df['listed_in'].values
print(transactions[:5])
