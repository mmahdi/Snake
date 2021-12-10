# Function that compute the weight of a particle if it touches the snake
def particle_weights(partic, measure):
    if measure[int(partic[0]) - 1, int(partic[1]) - 1] == 1:
        weight = 1    

    else:
        weight = 0

    return weight