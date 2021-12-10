import numpy as np
from prediction_model import prediction_model_1,prediction_model_2
from particle_weights import particle_weights
from measurement import measurement
from head_indice import is_near_head,is_on_head,snake_head_indice


def particle_filter_model_1(Particle_t, measure, number_particles, px):
    weight_t = np.ones(number_particles)
    particle_ = []
    
    for i in range(number_particles):
        Particle_t[i] = prediction_model_1(Particle_t[i])
        weight_t[i] = particle_weights(Particle_t[i], measure)
        particle_.append(weight_t[i] * Particle_t[i])

    # Indices of particles with w = 1    
    idex_part = np.flatnonzero(weight_t) 
    
    # Resampling
    for i in range(number_particles):
        if (weight_t[i] == 0) and (len(idex_part) > 0):
            var = np.random.randint(len(idex_part))
            particle_[i] = prediction_model_1(particle_[idex_part[var]])
            
        elif weight_t[i] == 1:
            particle_[i] = particle_[i]
            
        else:
            particle_[i] = np.random.randint(1, px + 1, size=(2,))

    return particle_

def particle_filter_model_2(Particle_t, measure, number_particles, px):

    particle_ = [] 
    pixel = 200
    weight_t = np.ones(number_particles)

    for i in range (number_particles):
        #another random movement for the particles
        Particle_t[i] = prediction_model_1(Particle_t[i])
        # boolean = is_on_head(Particle_t[i], px)
        # if boolean == 1:
        # j = i;
        # particles on the snake will be assigned to weight = 1 otherwise weight will be zero
        weight_t[i] = particle_weights(Particle_t[i], measure)
        particle_.append(Particle_t[i] * weight_t[i])
    loc_snake = np.flatnonzero(weight_t) # determining the indices where the snake is located

    # Resampling the particles

    for i in range (int (number_particles/1)):

        if ((weight_t[i] == 0) and len(loc_snake)>0):
        
            #we need to allocate the particle which is not on the snake to a place near the snake
            # This could be allocated by moving this particle to a place near the particle which is on the snake
            #P[i] = Movement_Particle_Model(P[L[random]], Head_Indice) # assign the particle that is not on the snake to a place near the snake
            particle_[i] = prediction_model_2(particle_[i], px)
        elif weight_t[i] == 1:

            particle_[i] = particle_[i] # if the particle has a weight of W = 1 , then it is on the snake and we don't move it

        else:
            # if there is not particles on the snake, then we initialize Particles again as done in the main with first initialization
            particle_[i] = np.random.randint(1, pixel +1, size=(2, ))

    return particle_