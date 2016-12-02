#!/usr/bin/python3

# Load in Required libraries
import math, numpy, time

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Scene:

    def mouse(self, button, state, x, y):
        print ("['mouse', "+str(button)+", "+str(state)+", "+str(x)+", "+str(y)+"]")
        self.lastX = x
        self.lastY = y
        glutPostRedisplay()

    def motion(self, x, y):
        self.angle -= (math.pi/180)*(self.lastX - x)
        self.up    -= (math.pi/180)*(self.lastY - y)
        print ("[(Xangle, Yangle), ("+str(self.angle)+", "+str(self.up)+")]")

        self.lastX = x
        self.lastY = y
        glutPostRedisplay()

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
        self.up = 0.0
        self.length = 5.0
        self.radius = 18.0
        self.stepSizeX = 5
        self.stepSizeY = 5
        self.lastX = 0
        self.lastY = 0
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        #glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowPosition(100,50)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Lab 08 - Part 4")
        glutDisplayFunc(self.display)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glutSpecialFunc(self.keyboardSpecial)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutMainLoop()

    def getCam(self):
        x = self.radius*math.cos(self.angle)*math.sin(self.up)
        y = self.radius*math.sin(self.angle)*math.sin(self.up)
        if self.up == 0:
            z = 0
        else:
            z = math.sqrt(pow(self.radius, 2) - pow(x,2) - pow(y,2))
        return x, z, y

    # Build the scene
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        gluLookAt(self.radius*math.cos(self.angle)*math.cos(self.up), self.radius*math.sin(self.up), self.radius*math.sin(self.angle)*math.cos(self.up), 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        glTranslatef(0,4,-4)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-4,0,0)

        glTranslatef(0,0,4)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-4,0,0)

        glTranslatef(0,0,4)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-4,-4,-8)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-4,0,0)

        glTranslatef(0,0,4)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-4,0,0)

        glTranslatef(0,0,4)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-4,-4,-8)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-4,0,0)

        glTranslatef(0,0,4)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-4,0,0)

        glTranslatef(0,0,4)

        glTranslatef(-4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(4,0,0)
        glutWireCube(4.0)
        glTranslatef(-10,0,0)

        glPopMatrix()

        glutSwapBuffers()
        #glFlush()

if __name__ == '__main__':
    myProgram = Scene()
