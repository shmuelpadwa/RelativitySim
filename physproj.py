from __future__ import print_function

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np
import math

import sys
import time
print ("Hello! Welcome to Shmu and Kate's amazing relativity simulator!!")
time.sleep(2)
print ("Above your head, on Halloween night, you see a bat flying, very fast!\nYou stand at the origin")
time.sleep(2)
beta = input("Please enter your desired, velocity, in terms of c. And please don't make the bat travel at c, because that isn't possible \n")
d = input("How far displaced from the acutal do you want the observed bat to be? For viewing purpose only. Recommended is 20 \n")
'''beta = 0.9999
d = 20'''
fig = plt.figure()


def make_axes(p,q):
    axes = plt.gca()
    #axes.set_xlim([p-50,p+50])
    #axes.set_ylim([q+d-30, q+d])
    axes.set_xlim([-200, 200])
    axes.set_ylim([0, 50])
    
    
    gamma = 1/math.sqrt(1-beta**2)
    #d=10 #distance of front of the object from the orgin
    
    #actual Bat
    actbatx = [p, p+1, p+2.5, p+4, p+6, p+3.5, p+1.5, p+0.5, p-2, p-3.5, p-4.5, p-5, p-6, p-8, p-9.5, p-11, p-12, p-14, p-16, p-15.5, p-16.5, p-19, p-20, p-21, p-18, p-16, p-15, p-14, p-12.5, p-11, p-9.5, p-9.5, p-8.5, p-7.5, p-7, p-7.5, p-7, p-6, p-4, p-2, p]
    actbaty = [q, q-1, q-2, q-2.5, q-3, q-3.5, q-4.5, q-5.5, q-5.5, q-6, q-7, q-8, q-7.5, q-7, q-7.5, q-8.5, q-6, q-4.5, q-4.5, q-2, q-0.5, q, q+3, q+4.5, q+4.5, q+4.5, q+5, q+2, q-0.5, q-2, q, q-1, q-1, q-1.5, q-1, q-3, q-3.5, q-3, q-2, q-1, q]
    actbatleftx = [p-11.5, p-11, p-11, p-11.5]
    actbatlefty = [q-2, q-1.5, q-1.5, q-2]
    actbatrightx = [p-9.5, p-8.5, p-8.5, p-9.5]
    actbatrighty = [q-2.5, q-2, q-2.5, q-2]
    seebatx = [(gamma*gamma *actbatx[40] - beta * gamma * math.sqrt(gamma*gamma*actbatx[40]*actbatx[40] + actbaty[40]*actbaty[40]))] * 41
    seebaty = [actbaty[40] + d] * 41
    seebatleftx = [(gamma*gamma *actbatleftx[3] - beta * gamma * math.sqrt(gamma*gamma*actbatleftx[3]*actbatleftx[3] + actbatlefty[3]*actbatlefty[3]))] * 4
    seebatlefty = [actbatlefty[3] + d] * 4
    seebatrightx = [(gamma*gamma *actbatrightx[3] - beta * gamma * math.sqrt(gamma*gamma*actbatrightx[3]*actbatrightx[3] + actbatrighty[3]*actbatrighty[3]))] * 4
    seebatrighty = [actbatrighty[3] + d] * 4
    for x in range(0,40):
        seebatx[x] = gamma*gamma *actbatx[x] - beta * gamma * math.sqrt(gamma*gamma*actbatx[x]*actbatx[x] + actbaty[x]*actbaty[x])
        seebaty[x] = actbaty[x] + d
    for x in range(0,3):
        seebatleftx[x] = gamma*gamma *actbatleftx[x] - beta * gamma * math.sqrt(gamma*gamma*actbatleftx[x]*actbatleftx[x] + actbatlefty[x]*actbatlefty[x])
        seebatlefty[x] = actbatlefty[x] + d
        seebatrightx[x] = gamma*gamma *actbatrightx[x] - beta * gamma * math.sqrt(gamma*gamma*actbatrightx[x]*actbatrightx[x] + actbatrighty[x]*actbatrighty[x])
        seebatrighty[x] = actbatrighty[x] + d

    axes.set_facecolor('#EB6123')
    axes.plot(actbatx, actbaty, linewidth = 0)
    plt.fill(actbatx, actbaty, facecolor = 'black', edgecolor = 'navy')
    axes.plot(seebatx, seebaty, linewidth = 0)
    plt.fill(seebatx, seebaty, facecolor = 'lightsalmon', edgecolor = 'orange')
    axes.plot(actbatleftx, actbatlefty, linewidth = 0)
    plt.fill(actbatleftx, actbatlefty, facecolor = 'yellow')
    axes.plot(actbatrightx, actbatrighty, linewidth = 0)
    plt.fill(actbatrightx, actbatrighty, facecolor = 'yellow')
    axes.plot(seebatleftx, seebatlefty, linewidth = 0)
    plt.fill(seebatleftx, seebatlefty, facecolor = 'red')
    axes.plot(seebatrightx, seebatrighty, linewidth = 0)
    plt.fill(seebatrightx, seebatrighty, facecolor = 'red')

    #plt.show(block)
    #fig.canvas.draw()
    #fig.canvas.flush_events()
    #plt.show()
    if p > 201:
        plt.close()
        
        sys.exit(0)
    return axes

plt.show(block=False)
for p in xrange(-200,202,2):
    print('About to doit with %d' % p)
    ax = make_axes(p,20)

    fig.add_subplot(ax)
    fig.canvas.draw()
    fig.canvas.flush_events()
    #time.sleep(0.01)
    fig.delaxes(ax)
time.sleep(2)

sys.exit(0)
