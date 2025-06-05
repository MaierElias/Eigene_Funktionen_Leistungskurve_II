#%%
import pandas as pd
import numpy as np
import plotly.express as px
# %%
#Tabelle erstellen
df = pd.read_csv('data/activity.csv')
df_select = df[['PowerOriginal','Duration', 'HeartRate' ]]
print(df_select)
# %%
#Sortieren der Tabelle nach Power und Zeit
power_duration = df_select.groupby('PowerOriginal')['Duration'].sum().reset_index()
print(power_duration)

# %%
#Diagramm erstellen
fig = px.scatter(power_duration, x='Duration', y='PowerOriginal',
             labels={'PowerOriginal': 'Power [W]', 'Duration': 'Zeit [s]'},
             title='Verbrachte Zeit pro Power-Stufe')
fig.show()
    
# %%
