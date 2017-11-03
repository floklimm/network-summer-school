# -*- coding: utf-8 -*-

# import necessary library
import numpy as np

# define a function 
def path_graph( n ):
    """
        Returns the (n x n) adjacency matrix 
        of a path graph with n nodes.
    """

    # empty adjacency matrix of shape (n x n)
    A = np.zeros((n,n))

    # loop over every node besides the last one
    for u in range(0, n-1):

        # connect this node to the subsequent one
        A[u,u+1] = 1

    A = A + np.transpose(A)

    # the matrix will now be returned
    return A

# call the function to obtain an adjancency matrix
# for a path graph of 10 nodes
path_10 = path_graph(10)

# put the matrix on screen in text
print(path_10)
