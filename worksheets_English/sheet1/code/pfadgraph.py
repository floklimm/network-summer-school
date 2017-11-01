# -*- coding: utf-8 -*-
# Importieren von benoetigten Bibliotheken
import numpy as np
# Definieren der Funktion
def pfadgraph( n ):
   "Erzeugt die Adjazenzmatrix eines Pfadgraphen auf n Knoten."
   A=np.zeros((n,n)) # Leere Adjazenzmatrix der Groesse n x n
   for x in range(0, n-1): # gehe ueber jeden Knoten
       A[x,x+1]=1 # und verbinde ihn mit dem naechsten
   A=A+np.transpose(A) # Transponieren und Addieren der Matrix um zu symmetrisieren
   return A # das Objekt A wird von der Funktion zurueck gegeben

pfad10=pfadgraph(10) # Ruft die Funktion auf um einen Pfad aus 10 Knoten zu erstellen
print(pfad10) # gibt die Matrix als Text in der Konsole aus
