# -*- coding: utf-8 -*-
"""
Created on Mon March 28 16:02:35 2022

@author: VIRAJ RANADE
"""

import numpy as np

## The Problem utilises 3 parts, thus n = 3
## We need to create 3 local stiffness matrices and stack them into a Global Stiffness matrix.
def create_stiffness(E,I,L):
    k = E*I/(L**3)
    
    K = k*np.array(([12,6*L,-12,6*L,6*L,4*L*L,-6*L,2*L*L,-12,-6*L,12,-6*L,6*L,2*L*L,-6*L,4*L*L]))
    K = K.reshape(4,4)
    return K
    

def global_stiffness(n,set_E,set_I,set_L):
    mat = np.zeros((2*n+2,2*n+2))
    
    for i in range(n):
        start = 2*i
        end = 2*i + 4
        
        #print(start,end)
        E,I,L = set_E[i],set_I[i],set_L[i]
        
        mat[start:end,start:end] += create_stiffness(E, I, L)
    
    return mat

def FEM(n,set_E,set_I,set_L,F):
    '''
    In the FEM Method we have 2 unknown forces, and the rest known for a cantilever.
    For Deflections, the corresponding deflections are known to be 0.
    Thus we can consider the m-2,m-2 matrix and invert it with the F vector to get
    the unknown displacements which we require.
    We are also returning The forces at the cantilever clamp.
    '''
    known_load_vec = np.array((0,0,0,0,F,0)).reshape(6,1)
    G = global_stiffness(n, set_E, set_I, set_L)
    G2 = G[2:8,2:8]
    G_I = np.linalg.inv(G2)
    
    deflections = G_I@known_load_vec
    
    total_def = np.vstack((np.array((0,0)).reshape(2,1),deflections))
    print(total_def)
    
    f1y = G[0]@total_def
    m1z = G[1]@total_def
    
    return (f1y,m1z,total_def)
    

    
    
    
    
    
    