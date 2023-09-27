from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import matplotlib.pyplot as plt



data = pd.read_csv('data/testData_month_orig.csv')
df = pd.DataFrame(data)

bar_df = df.iloc[0, [5, 6, 7, 8, 9, 10, 11, 12]]
n_df = pd.DataFrame(bar_df)
n_df.reset_index(inplace=True)
n_df.rename(
    columns={"index": "Hours", 0: "No of Calls"},
    inplace=True
)
color_dict = {'calls_at_9':'white',
              'calls_at_10':'white',
              'calls_at_11':'pink',
              'calls_at_12':'pink',
              'calls_at_13':'gold',
              'calls_at_14':'gold',
              'calls_at_15':'black',
              'calls_at_16':'black'}
app = Dash(__name__)

fig = px.bar(n_df, x='Hours', y='No of Calls', title='Todays Calls',color='Hours',color_discrete_map=color_dict)



app.layout= html.Div([
    html.Div([
            html.H1('Todays Calls'),
            dcc.Graph(
                id='bar-plot',
                figure=fig,
                style={'width':'45%', 'height':'50%'})
                ])])


if __name__ == '__main__':
    app.run(debug=True)