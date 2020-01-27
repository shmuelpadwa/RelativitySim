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
beta = 0
while beta > 1 or beta <= 0:
    beta = input("Please enter your desired velocity in terms of c. Between zero and one. Don't include the c. \nAlso, once you've enjoyed this, type the speed as 1 to access the secret mode!\n")
if beta != 1:
    
    d = input("How far displaced from the acutal do you want the observed bat to be? For viewing purpose only. Recommended is 10 \n")
    xd = input("How far do you want the bat to fly, in meters? Recommended is 200 for a long trip that allows you to see the extremes, or 50 for a quick journey that focuses on the important parts? Due to the y-axis' length, a distance of 50 will maintain the bat's proportions.\n")
    '''beta = 0.9999
    d = 20'''
    fig = plt.figure()


    def make_axes(p,q):
        axes = plt.gca()
        axes.set_xlim([-xd, xd])
        axes.set_ylim([-50, 50])
        ''' the x limit and y limit of the axes can be changed as wished'''
    
        gamma = 1/math.sqrt(1-beta**2)
        #d=10 #distance of front of the object from the orgin
    
        #actual Bat
        actbatx = [p, p+1, p+2.5, p+4, p+6, p+3.5, p+1.5, p+0.5, p-2, p-3.5, p-4.5, p-5, p-6, p-8, p-9.5, p-11, p-12, p-14, p-16, p-15.5, p-16.5, p-19, p-20, p-21, p-18, p-16, p-15, p-14, p-12.5, p-11, p-9.5, p-9.5, p-8.5, p-7.5, p-7, p-7.5, p-7, p-6, p-4, p-2, p]
        actbaty = [q, q-1, q-2, q-2.5, q-3, q-3.5, q-4.5, q-5.5, q-5.5, q-6, q-7, q-8, q-7.5, q-7, q-7.5, q-8.5, q-6, q-4.5, q-4.5, q-2, q-0.5, q, q+3, q+4.5, q+4.5, q+4.5, q+5, q+2, q-0.5, q-2, q, q-1, q-1, q-1.5, q-1, q-3, q-3.5, q-3, q-2, q-1, q]
        actbatleftx = [p-11.5, p-11, p-11, p-11.5] #the left eye
        actbatlefty = [q-2, q-1.5, q-1.5, q-2]
        actbatrightx = [p-9.5, p-8.5, p-8.5, p-9.5] # the right eye
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
        if p > xd+1:
            plt.close()
        
            sys.exit(0)
        return axes
    plt.show(block=False)
    for p in xrange(-xd,xd+2,2):
        print('About to doit with %d' % p)
        ax = make_axes(p,20)

        fig.add_subplot(ax)
        fig.canvas.draw()
        fig.canvas.flush_events()
        #time.sleep(0.01)
        fig.delaxes(ax)
    time.sleep(2)

    sys.exit(0)
else:
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
        #plt.gca().invert_yaxis()
        plt.show()
        new_shapes = change_shapes(linebuilder.shape)
        return new_shapes

    img = np.zeros((20,20,3),dtype='uint')
    shapes = create_shape_on_image(img)[0]
    print(shapes)
    beta = input("Please enter your desired velocity in terms of c. And please don't make the bat travel at c, because that isn't possible \n")
    d = input("How far displaced from the acutal do you want the observed bat to be? For viewing purpose only. Recommended is 10 \n")
    xd = input("How far do you want the bat to fly, in meters? Recommended is 200 for a long trip that allows you to see the extremes, or 50 for a quick journey that focuses on the important parts? Due to the y-axis' length, a distance of 50 will maintain the bat's proportions.\n")
    fig = plt.figure()
    def make_axes(p,q):
        axes = plt.gca()
        axes.set_xlim([-xd, xd])
        axes.set_ylim([-50, 50])
    
        gamma = 1/math.sqrt(1-beta**2)
        # We added midpoints, and midpoints between the midpoints, to give the curvy effect on the object as seen by the viewer.
        actshapex = [shapes[len(shapes)-1][0]] * (4 * (len(shapes) - 1) + 1)
        actshapey = [shapes[len(shapes)-1][1]] * (4 * (len(shapes) - 1) + 1)
        actshapex[0] = p
        actshapey[0] = q
        for s in range(4, (4 * (len(shapes) - 1) + 1), 4):
            actshapex[s] = p - shapes[0][0] + shapes[s/4][0]
            actshapey[s] = q - shapes[0][1] + shapes[s/4][1]
        for s in range(2, (4 * (len(shapes) - 1) + 1), 4):
            actshapex[s] = (actshapex[s-2] + actshapex[s+2])/2
            actshapey[s] = (actshapey[s-2] + actshapey[s+2])/2
        for s in range(1, (4 * (len(shapes) - 1) + 1), 2):
            actshapex[s] = (actshapex[s-1] + actshapex[s+1])/2
            actshapey[s] = (actshapey[s-1] + actshapey[s+1])/2
        seeshapex = [(gamma*gamma *actshapex[len(actshapex)-1] - beta * gamma * math.sqrt(gamma*gamma*actshapex[len(actshapex)-1]*actshapex[len(actshapex)-1] + actshapey[len(actshapey)-1]*actshapey[len(actshapey)-1]))] * (4 * (len(shapes) - 1) + 1)
        seeshapey = [actshapey[len(actshapey)-1] + d] * (4 * (len(shapes) - 1) + 1)
        for x in range(0, (4 * (len(shapes) - 1) + 1)):
            seeshapey[x] = actshapey[x] + d
            seeshapex[x] = gamma*gamma *actshapex[x] - beta * gamma * math.sqrt(gamma*gamma*actshapex[x]*actshapex[x] + actshapey[x]*actshapey[x])
        axes.set_facecolor('#EB6123')
        axes.plot(actshapex, actshapey, linewidth = 0)
        plt.fill(actshapex, actshapey, facecolor = 'black', edgecolor = 'navy')
        axes.plot(seeshapex, seeshapey, linewidth = 0)
        plt.fill(seeshapex, seeshapey, facecolor = 'lightsalmon', edgecolor = 'orange')
        if p > xd+1:
            plt.close()
            sys.exit(0)
        return axes

    plt.show(block=False)
    for p in xrange(-xd,xd+2,2):
        print('About to doit with %d' % p)
        ax = make_axes(p,20)

        fig.add_subplot(ax)
        fig.canvas.draw()
        fig.canvas.flush_events()
        #time.sleep(0.05)
        fig.delaxes(ax)
    time.sleep(2)

    sys.exit(0)
