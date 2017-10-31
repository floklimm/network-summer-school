# -*- coding: utf-8 -*-
# Importiere Bibliotheken
import matplotlib.pyplot as plt
import networkx as nx

# lade die Funktion pfadgraph aus der Datei pfadgraph.py
# (die Datei zaehlt als python-Modul)
from pfadgraph import pfadgraph

pfad10 = pfadgraph(10) # Ruft die Funktion auf um einen Pfad aus 10 Knoten zu erstellen
G = nx.from_numpy_matrix(pfad10) # schreibe die Adjazenzmatrix in ein anderes Objekt
nx.draw(G)  # die Funktion die das eigentliche zeichnen übernimmt
