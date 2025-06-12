
import pandas as pd
import numpy as np
import plotly.graph_objects as go

# erstellen der Tabelle aus den Daten
def create_table(input_data):
    """
    Erstellt eine Tabelle aus einem DataFrame mit den angegebenen Spalten.
    """
    if isinstance(input_data, str) and input_data.lower().endswith('.csv'):
        df = pd.read_csv(input_data)
        df_select = df[['PowerOriginal','Duration', 'HeartRate']]
        return df_select
    if input_data.lower().endswith('.npy'):
        input_data = np.load(input_data)
        # Annahme: Die Spaltenreihenfolge ist PowerOriginal, Duration, HeartRate
        df = pd.DataFrame(input_data, columns=['PowerOriginal', 'Duration', 'HeartRate'])
        df_select = df[['PowerOriginal', 'Duration', 'HeartRate']]
        return df_select
    elif isinstance(input_data, pd.DataFrame):
        # Annahme: Der DataFrame hat die Spalten PowerOriginal, Duration, HeartRate
        df_select = input_data[['PowerOriginal', 'Duration', 'HeartRate']]
        return df_select
    else:
        print("Ungültiger Dateityp oder Dateipfad.")
        print("\033[31mBitte brechen Sie das Programm mit Strg+C ab und starten Sie es erneut mit pdm run main.py.\033[0m")
        return None
    

# Hier wird der DataFrame gefiltert um die Leistungskurve zu erstellen
def create_leistungskurve(df_select):
    """
    Erstellt eine Leistungskurve (Power Duration Curve) aus dem DataFrame.
    """
    
    max_duration = int(df_select["Duration"].sum())  # z.B. bis 1 Stunde
    step = int(df_select["Duration"].mean())  # entprechende Abstände in Sekunden

    durations = []
    max_powers = []

    for window in range(1, max_duration + 1, step):
        rolling = df_select['PowerOriginal'].rolling(window, min_periods=window).mean()
        max_power = rolling.max()
        if not np.isnan(max_power):
            durations.append(window)
            max_powers.append(max_power)

    max_minutes = max_duration / 60
    tickvals = []
    base_ticks = [2, 5, 10]
    exp = -2  # Start bei 10^-2 = 0,01
    while True:
        for b in base_ticks:
            tick = b * (10 ** exp)
            if tick < 0.02:
                continue
            if tick > max_minutes:
                break
            tickvals.append(tick)
        if tick > max_minutes:
            break
        exp += 1

    ticktext = [
        f"{int(v*60)} s" if v < 1 else f"{round(v, 2)} min"
        for v in tickvals
    ]

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
            tickvals=tickvals,
            ticktext=ticktext
        )
    )
    
    df = pd.DataFrame({"durations": durations, "max_powers": max_powers})

    return df, fig

if __name__ == "__main__":
    input_data = 'data/activity.csv'
    df, fig = create_leistungskurve(create_table(input_data))
    fig.show(renderer='browser')  # Anzeige im Browser
  