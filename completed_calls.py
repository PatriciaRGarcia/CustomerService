import plotly.express as px
import pandas as pd



df = pd.read_csv("CustomerService/data/testData_month_orig.csv")

row_0 = df.iloc[0]

total_calls = row_0['calls_at_9'] + row_0['calls_at_10'] + row_0['calls_at_11'] + row_0['calls_at_12'] + row_0['calls_at_13'] + row_0['calls_at_14']+ row_0['calls_at_15'] + row_0['calls_at_16']

print(f"Completed calls so far: {total_calls}")

