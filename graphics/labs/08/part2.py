#!/usr/bin/python3

# Load in Required libraries
import math, numpy, time

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Scene:

    def keyboardSpecial(self, key, x, y):
        if key == 102:
            self.angle += .0174533
        elif key == 100:
            self.angle -= .0174533
        if key == 104:
            if self.stepSizeX > 1:
                self.stepSizeX -= 1
            if self.stepSizeY > 1:
                self.stepSizeY -= 1
        elif key == 105:
            if self.stepSizeX <= 180:
                self.stepSizeX += 1
            if self.stepSizeY <= 180:
                self.stepSizeY += 1
        glutPostRedisplay()


    def __init__(self):
        self.width = 400
        self.height = 400
        self.timeStep = 0
        self.timeStepSize = 0.02
        self.angle = 0.0
        self.length = 5.0
        self.radius = 30.0
        self.stepSizeX = 5
        self.stepSizeY = 5
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        #glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowPosition(100,50)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Lab 08 - Part 2")
        glutDisplayFunc(self.display)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glutSpecialFunc(self.keyboardSpecial)
        glutMainLoop()

    # Build the scene
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        gluLookAt(60*math.cos(self.angle), 0.0, 60*math.sin(self.angle), 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


        #start drawing sphere math
        glColor3f(1.0, 1.0, 1.0)
        glBegin(GL_POINTS)

        for angleX in range(0,360,self.stepSizeX):
            for angleY in range(0, 360, self.stepSizeY):
                radX = angleX * math.pi / 180
                radY = angleY * math.pi / 180
                x = self.radius*math.cos(radX)*math.sin(radY)
                y = self.radius*math.sin(radX)*math.sin(radY)
                z = self.radius*math.cos(radY)
                glVertex3f(x,y,z)

        glEnd()
        #end drawing sphere
        glPopMatrix()

        glutSwapBuffers()
        #glFlush()

if __name__ == '__main__':
    myProgram = Scene()
