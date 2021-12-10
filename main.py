from measurement import measurement
from particle_filter import particle_filter_model_1, particle_filter_model_2
from display_particles import display_particles
from head_indice import snake_head_indice
import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import cv2


# Global variables
number_particles = 1000 # number of desired particles
number_images = 1019 # number of frames available in the snake_color folder
px = 200 # Image size: 200x200
Particles = [] #List containing the particles
Particles_2 = [] #List containing the particles for model 2

# Display the images
#figure_ = plt.figure()
#ax = figure_.add_subplot(111)
#plt.ion()
#plt.show()

 # Initialize particles
for i in range(number_particles):
    Particles.append(np.random.randint(1, px + 1, size=(2,)))    
    Particles_2.append(np.random.randint(1, px + 1, size=(2,)))


###############################
# First model :snake follower #
###############################

# loop for all the images included in the snake_color folder
for i in range(number_images):
    img = imageio.imread("snake_color/snake_" + str(i).zfill(4) + ".png")
    Particles = particle_filter_model_1(Particles, measurement(img), number_particles, px)
    
    # Show each particle on the image in blue
    for j in range(number_particles):
        
        img[int(Particles[j][0]) - 1, int(Particles[j][1]) - 1, 1] = 0 # Remove the green color
        img[int(Particles[j][0]) - 1, int(Particles[j][1]) - 1, 2] = 255 # Max. value for the blue color channel
    #ax.imshow(img)
    #plt.show()
    #plt.draw()
    plt.imsave("results/snake_results_" + str(i).zfill(4) + ".png", img)


#dir = 'results/'
#display_particles(dir)

#####################################
# Second Case : snake head follower #
#####################################

img = imageio.imread("snake_color/snake_" + str(0).zfill(4) + ".png")
measure = measurement(img)
old_measure = measure


for i in range (number_images):
    img = imageio.imread("snake_color/snake_" + str(i+1).zfill(4) + ".png")
    measure = measurement(img)

    snake_head = snake_head_indice(measure, old_measure)
    Particles_2 = particle_filter_model_2(Particles_2, measure, number_particles, snake_head)

    old_measure = measure

    for j in range(number_particles):
        img[int(Particles_2[j][0]) - 1, int(Particles_2[j][1]) - 1, 1] = 0 # Remove the green color
        img[int(Particles_2[j][0]) - 1, int(Particles_2[j][1]) - 1, 2] = 255 # value for the blue color channel
    plt.imsave("results_head_follow/snake_results_head_follow" + str(i).zfill(4) + ".png", img)
