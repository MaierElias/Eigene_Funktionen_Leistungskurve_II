
import pandas as pd
import numpy as np
import plotly.graph_objects as go

#Tabelle erstellen
df = pd.read_csv('data/activity.csv')
df_select = df[['PowerOriginal','Duration', 'HeartRate' ]]
# print(df_select)


# Hier wird der DataFrame gefiltert um die Leistungskurve zu erstellen
max_duration = df_select["Duration"].sum()  # z.B. bis 1 Stunde
step = 1  # Schrittweite in Sekunden

durations = []
max_powers = []

for window in range(1, max_duration + 1, step):
    rolling = df_select['PowerOriginal'].rolling(window, min_periods=window).mean()
    max_power = rolling.max()
    if not np.isnan(max_power):
        durations.append(window)
        max_powers.append(max_power)


fig = go.Figure()
fig.add_trace(go.Scatter(x=np.array(durations) /60, # Umwandlung von Sekunden in Minuten 
                        y=max_powers,
                        mode='lines',
                        name='Power Duration Curve'))
fig.update_layout(
    xaxis_title='Dauer [min]',
    yaxis_title='Leistung [W]',
    title='Leistungskurve (Power Duration Curve)',
    xaxis_type='log',
    xaxis=dict(
        tickvals=[0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20],
        ticktext=['0.02', '0.05', '0.1', '0.2', '0.5', '1', '2', '5', '10', '20']
    )
)
fig.show(renderer='browser')  # 'png' for static image, 'browser' for interactive plot in browser
