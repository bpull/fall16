#!/usr/bin/python3

# Load in Required libraries
import math, numpy, time

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Our new Scene Class
class Scene:
    def __init__(self):
        self.width = 400
        self.height = 400
        self.timeStep = 0
        self.timeStepSize = 0.02
        self.angle = 0.0
        self.length = 5.0
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        #glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowPosition(100,50)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Part 2")
        glutDisplayFunc(self.display)
        glutIdleFunc(self.idle)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glutMainLoop()

    # Run the idle loop
    def idle(self):
        if (time.time() - self.timeStep) > self.timeStepSize:
            self.timeStep = time.time()
            self.angle += .0174
            glutPostRedisplay()

    def createTriangle(self,x1,x2,x3,y1,y2,y3,z1,z2,z3):
        glBegin(GL_TRIANGLES)
        glVertex3f(self.width/2 * x1, self.width/2 * y1, self.width/2 * z1)
        glVertex3f(self.width/2 * x2, self.width/2 * y2, self.width/2 * z2)
        glVertex3f(self.width/2 * x3, self.width/2 * y3, self.width/2 * z3)
        glEnd()

    # Build the scene
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #cube framework
        glPushMatrix()
        glColor3f(1.0, 0.0, 0.0)
        gluLookAt(10*math.cos(self.angle), 0.0, 10*math.sin(self.angle), 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glutWireCube(self.length)



        ############begin front face##############
        glColor3f(0.87,0.87,0.87)
        glBegin(GL_TRIANGLES)
        glVertex3f(-2.5, 2.5, -2.5)
        glVertex3f(-2.5, -2.5, -2.5)
        glVertex3f(2.5, -2.5, -2.5)
        glEnd()

        glColor3f(0.82,0.82,0.82)
        glBegin(GL_TRIANGLES)
        glVertex3f(-2.5, 2.5, -2.5)
        glVertex3f(2.5, 2.5, -2.5)
        glVertex3f(2.5, -2.5, -2.5)
        glEnd()


        # ############begin right face##############
        glColor3f(0.9,0.9,0.9)
        glBegin(GL_TRIANGLES)
        glVertex3f(2.5, 2.5, -2.5)
        glVertex3f(2.5, -2.5, -2.5)
        glVertex3f(2.5, -2.5, 2.5)
        glEnd()

        glColor3f(0.95,0.95,0.95)
        glBegin(GL_TRIANGLES)
        glVertex3f(2.5, 2.5, -2.5)
        glVertex3f(2.5, 2.5, 2.5)
        glVertex3f(2.5, -2.5, 2.5)
        glEnd()


        # ############begin back face##############
        glColor3f(0.8,0.8,0.8)
        glBegin(GL_TRIANGLES)
        glVertex3f(2.5, 2.5, 2.5)
        glVertex3f(-2.5, -2.5, 2.5)
        glVertex3f(-2.5, 2.5, 2.5)
        glEnd()

        glColor3f(0.75,0.75,0.75)
        glBegin(GL_TRIANGLES)
        glVertex3f(2.5, 2.5, 2.5)
        glVertex3f(-2.5, -2.5, 2.5)
        glVertex3f(2.5, -2.5, 2.5)
        glEnd()


        # ############begin left face##############
        glColor3f(0.7,0.7,0.7)
        glBegin(GL_TRIANGLES)
        glVertex3f(-2.5, 2.5, 2.5)
        glVertex3f(-2.5, -2.5, 2.5)
        glVertex3f(-2.5, -2.5, -2.5)
        glEnd()

        glColor3f(0.67,0.67,0.67)
        glBegin(GL_TRIANGLES)
        glVertex3f(-2.5, 2.5, 2.5)
        glVertex3f(-2.5, 2.5, -2.5)
        glVertex3f(-2.5, -2.5, -2.5)
        glEnd()


        # ############begin top face##############
        glColor3f(0.12,0.12,0.12)
        glBegin(GL_TRIANGLES)
        glVertex3f(2.5, 2.5, -2.5)
        glVertex3f(-2.5, 2.5, -2.5)
        glVertex3f(-2.5, 2.5, 2.5)
        glEnd()

        glColor3f(0.32,0.32,0.32)
        glBegin(GL_TRIANGLES)
        glVertex3f(-2.5, 2.5, 2.5)
        glVertex3f(2.5, 2.5, 2.5)
        glVertex3f(2.5, 2.5, -2.5)
        glEnd()


        # ############begin bottom face##############
        glColor3f(0.45,0.45,0.45)
        glBegin(GL_TRIANGLES)
        glVertex3f(2.5, -2.5, -2.5)
        glVertex3f(-2.5, -2.5, -2.5)
        glVertex3f(-2.5, -2.5, 2.5)
        glEnd()

        glColor3f(0.5,0.5,0.5)
        glBegin(GL_TRIANGLES)
        glVertex3f(2.5, -2.5, -2.5)
        glVertex3f(2.5, -2.5, 2.5)
        glVertex3f(-2.5, -2.5, 2.5)
        glEnd()



        glPopMatrix()

        glutSwapBuffers()
        #glFlush()

if __name__ == '__main__':
    myProgram = Scene()
