# -*- coding:utf-8 -*-

from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math

class Simulation:
    def __init__(self, X, Y, Z, n,lengthofweld):
        self.X = X
        self.Y = Y
        self.Z = Z
        self.n = n
        self.lengthofweld=lengthofweld
        self.font = {
                     'color': 'blue',
                     'weight': 'normal',
                     'size': 16,
                     }


    def simulate(self):
        fig = plt.figure()
        ax = fig.gca(projection='3d')
        i = 1
        j = 1
        while i <= self.n:
            xi = self.X[i - 1]
            yi = self.Y[i - 1]
            zi = self.Z[i - 1]
            while j <= i:
                y = np.linspace(0, self.lengthofweld, 100)
                x = y * 0 + xi[j - 1]
                z = zi[j - 1]
                ax.plot(x, y, z, zs=0)
                j = j + 1
            i = i + 1
            j = 1

        ax.set_xlabel('length of plate x', fontdict=self.font)
        ax.set_ylabel('width of plate y', fontdict=self.font)
        ax.set_zlabel('height of plate z', fontdict=self.font)
        plt.show()

    def simulateSection(self,area,angle,t):
        fig = plt.figure()
        area = area # 0 to 15 point radiuses
        x1 = t * math.tan(angle/2)

        plt.plot([-x1,0,x1],[t,0,t],linewidth=4, color='r')
        plt.plot([-x1,x1],[t,t],linewidth=4, color='r')
        i = 0
        while i < self.n:
            for x, y in zip(self.X[i], self.Z[i]):
                T = np.arctan2(x, y)
                plt.scatter(x, y, s=area,c=T, alpha=0.8, cmap=plt.cm.hsv)
            i += 1
        plt.show()
