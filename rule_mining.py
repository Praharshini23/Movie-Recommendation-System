rules = association_rules(
    frequent_itemsets,
    metric="lift",
    min_threshold=1
)

rules = rules.sort_values(
    by='lift',
    ascending=False
)

rules['antecedents'] = rules['antecedents'].apply(list)
rules['consequents'] = rules['consequents'].apply(list)

# Movie Genre Mapping

movie_genre_map = dict(
    zip(
        movies_df['title'],
        movies_df['listed_in']
    )
)
