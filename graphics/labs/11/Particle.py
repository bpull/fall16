from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


import numpy
import math, random

class Particle:

    def __init__(self, startPos, accel, num):
        self.startPos = startPos
        self.accel = numpy.array(accel)
        self.i = int(num)

        self.theta = numpy.random.uniform(0.0,20.0)
        self.phi = numpy.random.uniform(0.0,360.0)
        self.alpha = self.theta/20.0
        self.v_0 = self.getV_0()
        self.lag = .05 * self.i

    def getPos(self, clock):
        return self.startPos + (self.v_0*clock) + (0.5*self.accel*pow(clock,2))

    def getV_0(self):
        x = math.sin(numpy.radians(self.theta))* math.sin(numpy.radians(self.phi))
        y = math.cos(numpy.radians(self.theta))
        z = math.sin(numpy.radians(self.theta))*math.cos(numpy.radians(self.phi))
        velocity = numpy.array([x,y,z])
        return 90.0*(1 - pow(self.alpha,2))*velocity

    def drawMe(self, clock):
        pos = self.getPos(clock-self.lag)

        if (clock-self.lag) > 0:
            glBegin(GL_POINTS)
            glVertex3f(pos[0], pos[1], pos[2])
            glEnd()
