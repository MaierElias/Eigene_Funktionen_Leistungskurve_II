import numpy as np
import pandas as pd
import plotly.graph_objects as go

from functions import create_table, create_leistungskurve

# numpy_array = input("Wenn Sie einen NumPy-Array auswerten möchte eben Sie bitte den Pfad zur NumPy-Array-Datei ein: ")



input_data = input("Bitte geben Sie den Pfad zur auszuwertenden Datei ein (CSV oder NumPy-Array): ")
print("Eingabe:", input_data)

created_table = create_table(input_data)

ask_for_dataframe = input("Möchten Sie die den Dataframe anzeigen? (ja/nein): ").strip().lower()
if ask_for_dataframe == "ja":
    df, fig = create_leistungskurve(created_table)

    print(df)

ask_for_plot = input("Möchten Sie die Leistungskurve plotten? (ja/nein): ").strip().lower()
if ask_for_plot == "ja":
    print("Die Leistungskurve wird jetzt erstellt...")
    create_leistungskurve(created_table)
    fig.show(renderer='browser') # Anzeige im Browser

else: 
    print("Vielen Dank für die Nutzung des Programms!")
