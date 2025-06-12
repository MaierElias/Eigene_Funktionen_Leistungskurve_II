import numpy as np
import pandas as pd
import plotly.graph_objects as go

from functions import create_table, create_leistungskurve


input_data = input("Bitte geben Sie den Pfad zur auszuwertenden Datei ein (CSV oder NumPy-Array): ")
print("Eingabe:", input_data)

created_table = create_table(input_data)
df, fig = create_leistungskurve(created_table)

ask_for_dataframe = input("Möchten Sie die den Dataframe anzeigen? (ja/nein): ").strip().lower()
if ask_for_dataframe == "ja":
    print(df)

ask_for_plot = input("Möchten Sie die Leistungskurve plotten? (ja/nein): ").strip().lower()
if ask_for_plot == "ja":
    print("Die Leistungskurve wird jetzt erstellt...")
    fig.show(renderer='browser') # Anzeige im Browser
else: 
    print("Vielen Dank für die Nutzung des Programms!")
