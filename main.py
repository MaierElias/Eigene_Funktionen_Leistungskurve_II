import numpy as np
import pandas as pd
import plotly.graph_objects as go

from functions import create_table, create_leistungskurve

# numpy_array = input("Wenn Sie einen NumPy-Array auswerten möchte eben Sie bitte den Pfad zur NumPy-Array-Datei ein: ")



input_data = input("Geben Sie den Pfad zur auswertenden Datei ein (CSV oder NumPy-Array): ")
print("Eingabe:", input_data)

created_table = create_table(input_data)

ask_for_table = input("Möchten Sie die Tabelle anzeigen? (ja/nein): ").strip().lower()
if ask_for_table == "ja":
    print(created_table)

create_leistungskurve(created_table)

