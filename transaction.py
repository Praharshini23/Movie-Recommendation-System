
transactions = movies_df['listed_in'].tolist()

# One-Hot Encoding
te = TransactionEncoder()

te_array = te.fit(transactions).transform(transactions)

df_encoded = pd.DataFrame(
    te_array,
    columns=te.columns_
)
