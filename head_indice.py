import numpy as np

def snake_head_indice(Matrice, prev_Matrice):

    N = 200
    for i in range (N):
        for j in range (N):
            if Matrice[i][j]> prev_Matrice[i][j] :
                return i,j

    return 0,0

def is_near_head(Matrice, Head):
    if (abs(Head[0] - Matrice[0])<= 10 and abs(Head[1]-Matrice[1])<= 10):
        return 1
    return 0


def is_on_head(Particle,Head):
    
    if (Particle[0] == Head[0] and Particle[1] == Head[1]):
        return 1
    else:
        return 0
