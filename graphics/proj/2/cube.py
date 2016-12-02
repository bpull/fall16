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
        self.radius = 20.0
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

    def cornerPiece(self, r1,g1,b1,r2,g2,b2,r3,g3,b3, front, right, top):

        glColor3f(0,0,0)
        glutWireCube(5.0)

        glColor3f(r1,g1,b1)
        if front == 1:
            ############begin front face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glEnd()
        elif front == 0:
            # ############begin back face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(-2.5, 2.5, 2.5)
            glEnd()


            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()

        glColor3f(r2,g2,b2)
        if right == 1:
            # ############begin right face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()
        elif right == 0:
            # ############begin left face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glEnd()


        glColor3f(r3,g3,b3)
        if top == 1:
            # ############begin top face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, 2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(2.5, 2.5, -2.5)
            glEnd()
        elif top == 0:
            # ############begin bottom face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glEnd()


        glColor3f(0,0,0)




    def edgePiece(self, r1,g1,b1,r2,g2,b2, f,ba,r,l,t,bo):

        first = 1

        glColor3f(0,0,0)
        glutWireCube(5.0)

        if f == 1:
            if first == 1:
                glColor3f(r1,g1,b1)
                first = 0
            else:
                glColor3f(r2,g2,b2)
            ############begin front face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glEnd()

        if ba == 1:
            if first == 1:
                glColor3f(r1,g1,b1)
                first = 0
            else:
                glColor3f(r2,g2,b2)
            # ############begin back face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(-2.5, 2.5, 2.5)
            glEnd()


            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()

        if r == 1:
            if first == 1:
                glColor3f(r1,g1,b1)
                first = 0
            else:
                glColor3f(r2,g2,b2)
            # ############begin right face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()

        if l == 1:
            if first == 1:
                glColor3f(r1,g1,b1)
                first = 0
            else:
                glColor3f(r2,g2,b2)
            # ############begin left face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glEnd()

        if t == 1:
            if first == 1:
                glColor3f(r1,g1,b1)
                first = 0
            else:
                glColor3f(r2,g2,b2)
            # ############begin top face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, 2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(2.5, 2.5, -2.5)
            glEnd()

        if bo == 1:
            if first == 1:
                glColor3f(r1,g1,b1)
                first = 0
            else:
                glColor3f(r2,g2,b2)
            # ############begin bottom face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glEnd()

        glColor3f(0,0,0)

    def middlePiece(self, r,g,b, side):
        glColor3f(r,g,b)
        if side == 'front':
            ############begin front face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glEnd()
        elif side == 'back':
            # ############begin back face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(-2.5, 2.5, 2.5)
            glEnd()


            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()
        elif side == 'right':
            # ############begin right face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glEnd()
        elif side == 'left':
            # ############begin left face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glEnd()
        elif side == 'top':
            # ############begin top face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, 2.5, -2.5)
            glVertex3f(-2.5, 2.5, -2.5)
            glVertex3f(-2.5, 2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(-2.5, 2.5, 2.5)
            glVertex3f(2.5, 2.5, 2.5)
            glVertex3f(2.5, 2.5, -2.5)
            glEnd()
        elif side == 'bottom':
            # ############begin bottom face##############
            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(-2.5, -2.5, -2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glEnd()

            glBegin(GL_TRIANGLES)
            glVertex3f(2.5, -2.5, -2.5)
            glVertex3f(2.5, -2.5, 2.5)
            glVertex3f(-2.5, -2.5, 2.5)
            glEnd()
        glColor3f(0,0,0)


    # Build the scene
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glPushMatrix()
        gluLookAt(self.radius*math.cos(self.angle)*math.cos(self.up), self.radius*math.sin(self.up), self.radius*math.sin(self.angle)*math.cos(self.up), 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

        glColor3f(0,0,0)
        glTranslatef(0,5,-5)

        ################## top layer #######################

        glTranslatef(-5,0,0)
        self.cornerPiece(0,1,0, 1,.5,0, 1,1,0, 1,0,1)
        glTranslatef(5,0,0)
        self.edgePiece(0,1,0, 1,1,0, 1,0,0,0,1,0)
        glTranslatef(5,0,0)
        self.cornerPiece(0,1,0, 1,0,0, 1,1,0, 1,1,1)
        glTranslatef(-5,0,0)

        glTranslatef(0,0,5)

        glTranslatef(-5,0,0)
        self.edgePiece(1,.5,0, 1,1,0, 0,0,0,1,1,0)
        glTranslatef(5,0,0)
        self.middlePiece(1,1,0, 'top')
        glTranslatef(5,0,0)
        self.edgePiece(1,0,0, 1,1,0, 0,0,1,0,1,0)
        glTranslatef(-5,0,0)

        glTranslatef(0,0,5)

        glTranslatef(-5,0,0)
        self.cornerPiece(0,0,1, 1,.5,0, 1,1,0, 0,0,1)
        glTranslatef(5,0,0)
        self.edgePiece(0,0,1, 1,1,0, 0,1,0,0,1,0)
        glTranslatef(5,0,0)
        self.cornerPiece(0,0,1, 1,0,0, 1,1,0, 0,1,1)
        glTranslatef(-5,-5,-10)

        ################# middle layer ##########################

        glTranslatef(-5,0,0)
        self.edgePiece(0,1,0, 1,.5,0, 1,0,0,1,0,0)
        glTranslatef(5,0,0)
        self.middlePiece(0,1,0, 'front')
        glTranslatef(5,0,0)
        self.edgePiece(0,1,0, 1,0,0, 1,0,1,0,0,0)
        glTranslatef(-5,0,0)

        glTranslatef(0,0,5)

        glTranslatef(-5,0,0)
        self.middlePiece(1,.5,0, 'left')
        glTranslatef(5,0,0)
        glutWireCube(5.0)
        glTranslatef(5,0,0)
        self.middlePiece(1,0,0, 'right')
        glTranslatef(-5,0,0)

        glTranslatef(0,0,5)

        glTranslatef(-5,0,0)
        self.edgePiece(0,0,1, 1,.5,0, 0,1,0,1,0,0)
        glTranslatef(5,0,0)
        self.middlePiece(0,0,1, 'back')
        glTranslatef(5,0,0)
        self.edgePiece(0,0,1, 1,0,0, 0,1,1,0,0,0)
        glTranslatef(-5,-5,-10)

        #############bottom layer##############################
        glTranslatef(-5,0,0)
        self.cornerPiece(0,1,0, 1,.5,0, 1,1,1, 1,0,0)
        glTranslatef(5,0,0)
        self.edgePiece(0,1,0, 1,1,1, 1,0,0,0,0,1)
        glTranslatef(5,0,0)
        self.cornerPiece(0,1,0, 1,0,0, 1,1,1, 1,1,0)
        glTranslatef(-5,0,0)

        glTranslatef(0,0,5)

        glTranslatef(-5,0,0)
        self.edgePiece(1,.5,0, 1,1,1, 0,0,0,1,0,1)
        glTranslatef(5,0,0)
        self.middlePiece(1,1,1, 'bottom')
        glTranslatef(5,0,0)
        self.edgePiece(1,0,0, 1,1,1, 0,0,1,0,0,1)
        glTranslatef(-5,0,0)

        glTranslatef(0,0,5)

        glTranslatef(-5,0,0)
        self.cornerPiece(0,0,1, 1,.5,0, 1,1,1, 0,0,0)
        glTranslatef(5,0,0)
        self.edgePiece(0,0,1, 1,1,1, 0,1,0,0,0,1)
        glTranslatef(5,0,0)
        self.cornerPiece(0,0,1, 1,0,0, 1,1,1, 0,1,0)
        glTranslatef(-15,0,0)

        glPopMatrix()

        glutSwapBuffers()
        #glFlush()

if __name__ == '__main__':
    myProgram = Scene()
