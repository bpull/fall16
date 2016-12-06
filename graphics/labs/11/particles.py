import numpy, math, random
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class particle:
    def __init__(self, initialPos, initialVel, acceleration, i):
        self.initialPos = initialPos
        self.initialVel = initialVel
        self.acceleration = numpy.array(acceleration)
        self.i = i
        self.tLag = .05 * self.i
        self.theta = numpy.random.uniform(0.0,20.0)
        self.alpha = self.theta/20.0
        self.phi = numpy.random.uniform(0.0,360.0)
        self.determineInitVel()

    def determineInitVel(self):
        velocityX = math.sin(numpy.radians(self.theta))* math.sin(numpy.radians(self.phi))
        velocityY = math.cos(numpy.radians(self.theta))
        velocityZ = math.sin(numpy.radians(self.theta))*math.cos(numpy.radians(self.phi))
        velocity = numpy.array([velocityX, velocityY, velocityZ])
        self.initialVel = (90.0 * (1 - self.alpha**2))*velocity

    def determinePos(self, time):
        pos = self.initialPos + (self.initialVel * time) + (0.5 * self.acceleration * time**2)
        return pos

    def draw(self, time):
        position = self.determinePos(time-self.tLag)
        if time-self.tLag > 0:
            glBegin(GL_POINTS)
            glVertex3f(position[0], position[1], position[2])
            glEnd()
