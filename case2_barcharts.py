import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
from dash import Dash, html, dcc


data=pd.read_csv('CustomerService/data/testData_month_orig.csv')

data['sum'] = data[['calls_at_9', 'calls_at_10','calls_at_11','calls_at_12','calls_at_13','calls_at_14','calls_at_15','calls_at_16']].sum(axis=1)

plt.figure(figsize=(10,6))
plt.bar(x = data['date'],
        height = data['sum'],
        color='goldenrod')

plt.xticks(rotation= 45, fontsize = 10)
plt.yticks()
plt.title("Monthly Daily Calls", fontsize = 30, fontweight ='bold')
plt.ylabel('Amount of calls', fontsize = 15, color='midnightblue',fontweight='bold')
plt.xlabel('Day of month',fontsize= 15, color='midnightblue',fontweight='bold')

plt.show()



