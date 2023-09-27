import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from dash import Dash, html, dcc

data=pd.read_csv()

plt.figure(figsize=(16,9))
plt.bar(x = data['Day'],
        height = data['Calls'],
        color='goldenrod')
plt.xticks(rotation= 45, fontsize = 10)
plt.yticks(fontsize = 13)
plt.title("Monthly Daily Calls", fontsize = 30, fontweight ='bold')
plt.ylabel('Calls', fontsize = 25, color='midnightblue',fontweight='bold')
plt.xlabel('Date',fontsize= 25, color='midnightblue',fontweight='bold')

plt.show()



