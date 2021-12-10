import numpy as np
from matplotlib import pylab
#funtion that return a matrix representing the state
def measurement(image):
    (number_px, _, _) = image.shape 
    state = image[:, :, 0] == 255 * np.ones((number_px, number_px))
    return state

#image = pylab.imread('snake/snake_1001.png')
#measurement(image)