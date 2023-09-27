import plotly.express as px
import matplotlib.pyplot as plt
from dash import Dash, html, dcc



data = {
    'Busy': 66.67,
    'Available': 33.33
}

colors = ['tomato', 'lightgreen']

fig, ax = plt.subplots()
ax.pie(data.values(), labels=data.keys(), colors=colors, autopct='%1.1f%%', startangle=50)
plt.axis('equal') 

plt.title('Current employees currently active in support')
plt.show()