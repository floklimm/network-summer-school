# -*- coding: utf-8 -*-
# Importieren von benoetigten Bibliotheken
import numpy as np
# daten laden
H=np.loadtxt("huhn.txt")

H2 = H + np.transpose(H)
H2=H2
H3=np.ceil(H2)
np.savetxt("hennen.txt",H2, fmt='%1.0f')
