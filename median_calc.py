import pandas as pd

df = pd.read_csv('output_csv/RF_years.csv', sep = ',', header = None)
df1 = df.groupby([0])[1].median()
df.to_csv('output_csv/RF_years_grouped.csv')
