import plotly.express as px
import matplotlib.pyplot as plt
from dash import Dash, html, dcc



data = {
    'Workers': 66.67,
    'Vacant Positions': 33.33
}

colors = ['tomato', 'lightgreen']

fig, ax = plt.subplots()
ax.pie(data.values(), labels=data.keys(), colors=colors, autopct='%1.1f%%', startangle=50)
plt.axis('equal') 

plt.title('Total employees in support')
plt.show()