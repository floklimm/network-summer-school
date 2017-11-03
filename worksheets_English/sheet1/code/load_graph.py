# -*- coding: utf-8 -*-
# importing libraries
import numpy as np

# load data
H = np.loadtxt("huhn.txt")

#symmetrize 
H2 = H + np.transpose(H)
H2 = H2
H3 = np.ceil(H2)

np.savetxt("hennen.txt",H2, fmt='%1.0f')
