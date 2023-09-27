from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('data/testData_month_orig.csv')
df = pd.DataFrame(data)

bar_df = df.iloc[0, [5, 6, 7, 8, 9, 10, 11, 12]]
n_df = pd.DataFrame(bar_df)
print(n_df)

# hours_column = bar_df.iloc[:,1]
# no_calls_column = bar_df.iloc[:,2]
# mod_df = pd.DataFrame({'Hours': hours_column, 'No of Calls': no_calls_column})

# # Skapa en lista med kolumnnamnen
# hours_column = bar_df.columns.tolist()

# # Skapa en DataFrame med kolumnnamnen som "Hours" och data från bar_df som "No of Calls"
# mod_df = pd.DataFrame({'Hours': hours_column, 'No of Calls': bar_df.loc[1,].values.flatten()})

# app = Dash(__name__)

# fig = px.bar(mod_df, x='Hours', y='No of Calls', title='Todays Calls',color='Hours')



# app.layout= html.Div([
#     html.Div([
#             html.H1('Todays Calls'),
#             dcc.Graph(
#                 id='bar-plot',
#                 figure=fig,
#                 style={'width':'45%', 'height':'50%'})
#                 ])])


# if __name__ == '__main__':
#     app.run(debug=True)