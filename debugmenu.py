from __future__ import print_function
from matplotlib.animation import FuncAnimation
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import math
import sys
import time

class LineBuilder:
    def __init__(self, line,ax,color):
        self.line = line
        self.ax = ax
        self.color = color
        self.xs = []
        self.ys = []
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
        self.counter = 0
        self.shape_counter = 0
        self.shape = {}
        self.precision = 1

    def __call__(self, event):
        if event.inaxes!=self.line.axes: return
        if self.counter == 0:
            self.xs.append(event.xdata)
            self.ys.append(event.ydata)
        if np.abs(event.xdata-self.xs[0])<=self.precision and np.abs(event.ydata-self.ys[0])<=self.precision and self.counter != 0:
            self.xs.append(self.xs[0])
            self.ys.append(self.ys[0])
            self.ax.scatter(self.xs,self.ys,s=120,color=self.color)
            self.ax.scatter(self.xs[0],self.ys[0],s=80,color='blue')
            self.ax.plot(self.xs,self.ys,color=self.color)
            self.line.figure.canvas.draw()
            self.shape[self.shape_counter] = [self.xs,self.ys]
            self.shape_counter = self.shape_counter + 1
            self.xs = []
            self.ys = []
            self.counter = 0
        else:
            if self.counter != 0:
                self.xs.append(event.xdata)
                self.ys.append(event.ydata)
            self.ax.scatter(self.xs,self.ys,s=120,color=self.color)
            self.ax.plot(self.xs,self.ys,color=self.color)
            self.line.figure.canvas.draw()
            self.counter = self.counter + 1

def create_shape_on_image(data,cmap='jet'):
    def change_shapes(shapes):
        new_shapes = {}
        for i in range(len(shapes)):
            l = len(shapes[i][1])
            new_shapes[i] = np.zeros((l,2),dtype='int')
            for j in range(l):
                new_shapes[i][j,0] = shapes[i][0][j]
                new_shapes[i][j,1] = shapes[i][1][j]
        return new_shapes
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_title('Create your own! Click to include points, ending with first point. Close when done)')
    line = ax.imshow(data) 
    ax.set_xlim(0,data[:,:,0].shape[1])
    ax.set_ylim(0,data[:,:,0].shape[0])
    linebuilder = LineBuilder(line,ax,'red')
    plt.gca().invert_yaxis()
    plt.show()
    new_shapes = change_shapes(linebuilder.shape)
    return new_shapes

img = np.zeros((20,20,3),dtype='uint')
shapes = create_shape_on_image(img)[0]
print(shapes)
beta = input("Please enter your desired, velocity, in terms of c. And please don't make the bat travel at c, because that isn't possible \n")
d = input("How far displaced from the acutal do you want the observed bat to be? For viewing purpose only. Recommended is 10 \n")
fig = plt.figure()
def make_axes(p,q):
    axes = plt.gca()
    #axes.set_xlim([p-50,p+50])
    #axes.set_ylim([q+d-30, q+d])
    axes.set_xlim([-50, 50])
    axes.set_ylim([-50, 50])
    
    gamma = 1/math.sqrt(1-beta**2)
    actshapex = [shapes[len(shapes)-1][0]] * len(shapes)
    actshapey = [shapes[len(shapes)-1][1]] * len(shapes)
    actshapex[0] = p
    actshapey[0] = q
    for s in range(1, len(shapes)):
        actshapex[s] = p - shapes[0][0] + shapes[s][0]
        actshapey[s] = q - shapes[0][1] + shapes[s][1]
    seeshapex = [(gamma*gamma *actshapex[len(actshapex)-1] - beta * gamma * math.sqrt(gamma*gamma*actshapex[len(actshapex)-1]*actshapex[len(actshapex)-1] + actshapey[len(actshapey)-1]*actshapey[len(actshapey)-1]))] * 41
    seeshapey = [actshapey[len(actshapey)-1] + d] * 41
    for x in range(1, len(shapes)):
        seeshapey[x] = actshapey[x] + d
        seeshapex[x] = gamma*gamma *actshapex[x] - beta * gamma * math.sqrt(gamma*gamma*actshapex[x]*actshapex[x] + actshapey[x]*actshapey[x])
    axes.set_facecolor('#EB6123')
    axes.plot(actshapex, actshapey, linewidth = 0)
    plt.fill(actshapex, actshapey, facecolor = 'black', edgecolor = 'navy')
    axes.plot(seeshapex, seeshapey, linewidth = 0)
    plt.fill(seeshapex, seeshapey, facecolor = 'lightsalmon', edgecolor = 'orange')
    if p > 51:
        plt.close()
        
        sys.exit(0)
    return axes

plt.show(block=False)
for p in xrange(-50,52,2):
    print('About to doit with %d' % p)
    ax = make_axes(p,20)

    fig.add_subplot(ax)
    fig.canvas.draw()
    fig.canvas.flush_events()
    #time.sleep(0.01)
    fig.delaxes(ax)
time.sleep(2)

sys.exit(0)
