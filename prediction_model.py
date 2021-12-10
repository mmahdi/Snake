import numpy as np
import random
def prediction_model_1(particle):
    var = random.uniform(0, 1)
    if (0<var<0.25 and particle[0]<199):
        particle[0]+=1
    elif (0.25<var<0.5 and particle[0]>1):
        particle[0]-=1 
    elif (0.5<var<0.75 and particle[1]<199):
        particle[1]+=1
    elif (0.75<var<1 and particle[1]>1):
        particle[1]-=1
    return particle


def prediction_model_2(Part,target):
    Part[0] = target[0]
    Part[1] = target[1]
    var = random.uniform(0, 1)
    if (0<var<0.25 and Part[0]<199):
        Part[0]+=1
    elif (0.25<var<0.5 and Part[0]>1):
        Part[0]-=1 
    elif (0.5<var<0.75 and Part[1]<199):
        Part[1]+=1
    elif (0.75<var<1 and Part[1]>1):
        Part[1]-=1
    return Part
