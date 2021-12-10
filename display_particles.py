import os
import matplotlib.pyplot as plt

def display_particles(dir):

    figure_ = plt.figure()
    ax = figure_.add_subplot(111)
    plt.ion()
    plt.show()

    for fname in os.listdir(dir):
        fname = os.path.join(dir, fname)
        im = plt.imread(fname)
        img = ax.imshow(im)
        plt.draw()
        #accept = raw_input('OK? ')


dir = 'results/'
display_particles(dir)