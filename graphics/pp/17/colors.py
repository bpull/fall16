#!/usr/bin/python3

# Load in Required libraries
import math, numpy, time, makeTopoMap

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
        self.angle += (math.pi/180)*(self.lastX - x)
        self.up    += (math.pi/180)*(self.lastY - y)
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
        self.width = 800
        self.height = 800
        self.timeStep = 0
        self.timeStepSize = 0.02
        self.angle = -1.5708
        self.up = 0.0
        self.length = 5.0
        self.radius = 30.0
        self.stepSizeX = 5
        self.stepSizeY = 5
        self.lastX = 0
        self.lastY = 0
        self.threshold = 6.5
        self.rows = 10
        self.cols = 10
        self.M = makeTopoMap.get_matrix(rows=10, cols=10, seed=11317, maxval=8)
        self.colors = [(8,48,107), (8,81,156), (33, 113, 181), (66, 146, 198), (107, 174, 214), (158, 202, 225), (198, 219, 239), (222, 235, 247), (247, 251, 255)]

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        #glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowPosition(100,50)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Color Scheme")
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

    # Build the scene
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        gluLookAt((self.rows+10)*math.cos(self.angle)*math.cos(self.up), (self.rows+10)*math.sin(self.up), (self.rows+10)*math.sin(self.angle)*math.cos(self.up), 0.0, 0.0, 0.0, 0.0, -1.0, 0.0)


        for row in range(self.rows-1):
            for col in range(self.cols-1):

                glColor3f(1,1,1)
                glBegin(GL_TRIANGLES)

                x = col - (self.cols/2)
                y = row - (self.rows/2)
                z = self.M[row][col]

                r,g,b = self.colors[z]
                r /= 255.0
                g /= 255.0
                b /= 255.0
                glColor3f(r,g,b)
                glVertex3f(x, y, -z)

                x = (col+1) - (self.cols/2)
                y = row     - (self.rows/2)
                z = self.M[row][col+1]

                r,g,b = self.colors[z]
                r /= 255.0
                g /= 255.0
                b /= 255.0
                glColor3f(r,g,b)
                glVertex3f(x, y, -z)


                x = col     - (self.cols/2)
                y = (row+1) - (self.rows/2)
                z = self.M[row+1][col]

                r,g,b = self.colors[z]
                r /= 255.0
                g /= 255.0
                b /= 255.0
                glColor3f(r,g,b)
                glVertex3f(x, y, -z)

                glEnd()
                glBegin(GL_TRIANGLES)

                x = (col+1) - (self.cols/2)
                y = (row+1) - (self.rows/2)
                z = self.M[row+1][col+1]

                r,g,b = self.colors[z]
                r /= 255.0
                g /= 255.0
                b /= 255.0
                glColor3f(r,g,b)
                glVertex3f(x, y, -z)

                x = col     - (self.cols/2)
                y = (row+1) - (self.rows/2)
                z = self.M[row+1][col]

                r,g,b = self.colors[z]
                r /= 255.0
                g /= 255.0
                b /= 255.0
                glColor3f(r,g,b)
                glVertex3f(x, y, -z)

                x = (col+1) - (self.cols/2)
                y = row     - (self.rows/2)
                z = self.M[row][col+1]

                r,g,b = self.colors[z]
                r /= 255.0
                g /= 255.0
                b /= 255.0
                glColor3f(r,g,b)
                glVertex3f(x, y, -z)

                glEnd()

        #end drawing

        glPopMatrix()

        glutSwapBuffers()
        #glFlush()

if __name__ == '__main__':
    myProgram = Scene()
