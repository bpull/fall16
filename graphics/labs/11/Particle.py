from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy
import math, random

class Particle:

    def __init__(self, startPos, startVelo, startAccel):
        self.startPos = startPos
        self.startVelo = startVelo
        self.accel = startAccel
        self.i = i
        self.lag = .05 * self.i
        self.theta = numpy.random.uniform(0.0,20.0)
        self.alpha = self.theta/20.0
        self.phi = numpy.random.uniform(0.0,360.0)
        self.determineInitVel()


    def determinePos(self, time):
        pos = self.initialPos + (self.initialVel * time) + (0.5 * self.acceleration * time**2)
        return pos

    def determineInitVel(self):
        velocityX = math.sin(numpy.radians(self.theta))* math.sin(numpy.radians(self.phi))
        velocityY = math.cos(numpy.radians(self.theta))
        velocityZ = math.sin(numpy.radians(self.theta))*math.cos(numpy.radians(self.phi))
        velocity = numpy.array([velocityX, velocityY, velocityZ])
        self.initialVel = (90.0 * (1 - self.alpha**2))*velocity
        
    def doIT(self, clock):
        pos = self.getPos(clock-self.lag)

        if (clock-self.lag) > 0:
            glBegin(GL_POINTS)
            glVertex3f(pos[0], pos[1], pos[2])
            glEnd()
