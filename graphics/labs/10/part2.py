#!/usr/bin/python3

# Load in Required libraries
import math, numpy, time, makeTopoMap

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Scene:


    # arcball position function
    def zxy(self,x,y,w,h):
        if ((x - (w/2.0))**2 + (y - (h/2.0))**2) < ((h/2.0)**2):
            return numpy.sqrt((h/2.0)**2 - (x - (w/2.0))**2 - (y - (h/2.0))**2)
        return 0.01

    # arcball angle determination
    def vector_angle(self, p1, p2):
        # Calculate the angle between the two vectors
        theta = numpy.arccos((p1.dot(p2))/(numpy.linalg.norm(p2) * numpy.linalg.norm(p1)))
        # Calculate the axis of rotation (u)
        u = (numpy.cross(p1, p2) / (numpy.linalg.norm(p2) * numpy.linalg.norm(p1)))
        return theta, u

    # hit a key
    def keyboard(self, key, x, y):
        print(str(['keyboard-action', key, x, y]))
        glutPostRedisplay()

    # hit a special key
    def keyboardSpecial(self, key, x, y):
        print(str(['keyboard-special-action', key, x, y]))
        #glutPostRedisplay()

    # Click the mouse
    def mouse(self, button, state, x, y):
        z = self.zxy(x,y,self.width, self.height)
        x = -1.0 * (self.width/2.0 - x)
        y = self.height/2.0 - y
        if button == 0 and state == 0:
            self.wr.append([0.0, numpy.array([0,0,0])])
            self.P1 = numpy.array([x,y,z])

    # The mouse is clicked and held down
    # This is called no matter what button is being held down,
    # So you will want to track which buttons are down.
    def motion(self, x, y):
        z = self.zxy(x,y,self.width, self.height)
        x = -1.0 * (self.width/2.0 - x)
        y = self.height/2.0 - y
        self.P2 = numpy.array([x,y,z])
        theta, u = self.vector_angle(self.P1, self.P2)
        self.wr[-1] = [theta, u]
        glutPostRedisplay()

    # def mouse(self, button, state, x, y):
    #     print ("['mouse', "+str(button)+", "+str(state)+", "+str(x)+", "+str(y)+"]")
    #     self.lastX = x
    #     self.lastY = y
    #     glutPostRedisplay()
    #
    # def motion(self, x, y):
    #     self.angle += (math.pi/180)*(self.lastX - x)
    #     self.up    += (math.pi/180)*(self.lastY - y)
    #     print ("[(Xangle, Yangle), ("+str(self.angle)+", "+str(self.up)+")]")
    #
    #     self.lastX = x
    #     self.lastY = y
    #     glutPostRedisplay()
    #
    # def keyboardSpecial(self, key, x, y):
    #     if key == 102:
    #         self.angle += .0174533
    #     elif key == 100:
    #         self.angle -= .0174533
    #     if key == 104:
    #         if self.stepSizeX > 1:
    #             self.stepSizeX -= 1
    #         if self.stepSizeY > 1:
    #             self.stepSizeY -= 1
    #     elif key == 105:
    #         if self.stepSizeX <= 180:
    #             self.stepSizeX += 1
    #         if self.stepSizeY <= 180:
    #             self.stepSizeY += 1
    #     glutPostRedisplay()


    def __init__(self):
        self.width = 400
        self.height = 400
        self.camera = 10

        self.P1 = numpy.array([0,0,0])
        self.P2 = numpy.array([0,0,0])
        self.theta = 0.0
        self.u = numpy.array([0,0,0])
        self.wr = []

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
        self.M = makeTopoMap.get_matrix(rows=10, cols=10, seed=1117, maxval=8)

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        #glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowPosition(100,50)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Lab 10 - Part 2")
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

        glColor3f(1.0, 1.0, 1.0)

        glPushMatrix()

        # Translate the world based on the arcball
        glTranslatef(0.0,0.0,-self.camera)
        for i in range(len(self.wr)-1,-1,-1):
            r = self.wr[i]
            glRotatef(numpy.degrees(r[0]), r[1][0], r[1][1], r[1][2])

        # Working with the modelview matrix to determine current direction
        mvm = glGetFloatv(GL_MODELVIEW_MATRIX)
        mvm_x = mvm[:,0]
        mvm_y = mvm[:,1]
        mvm_z = mvm[:,2]
        mvm_l = mvm[2]
        mvm_u = mvm[1]
        mvm_r = mvm[0]
        mvm_c = mvm[3]
        mvm_cC = mvm * numpy.array([mvm_c]).T
        mvm_cC = mvm_cC[2]

        print("\x1b[H\x1b[2J")
        print('Modelview matrix=')
        print(mvm)

        print('')
        print('Xaxis      ='+str(mvm_x))
        print('Yaxis      ='+str(mvm_y))
        print('Zaxis      ='+str(mvm_z))
        print('')
        print('RightVector='+str(numpy.rint(mvm_r)))
        print('UpVector   ='+str(numpy.rint(mvm_u)))
        print('LookVector ='+str(numpy.rint(mvm_l)))

        print('')
        print('Camera     ='+str(mvm_c))
        print("Camera'    ="+str(mvm_cC))

        for row in range(self.rows-1):
            for col in range(self.cols-1):

                glColor3f(1,1,1)
                glBegin(GL_TRIANGLES)

                x = col - (self.cols/2)
                y = row - (self.rows/2)
                z = self.M[row][col]

                color = z*(0.7/8) + 0.3
                glColor3f(color, color, color)
                glVertex3f(x, y, -z)

                x = (col+1) - (self.cols/2)
                y = row     - (self.rows/2)
                z = self.M[row][col+1]

                color = z*(0.7/8) + 0.3
                glColor3f(color, color, color)
                glVertex3f(x, y, -z)


                x = col     - (self.cols/2)
                y = (row+1) - (self.rows/2)
                z = self.M[row+1][col]

                color = z*(0.7/8) + 0.3
                glColor3f(color, color, color)
                glVertex3f(x, y, -z)

                glEnd()
                glBegin(GL_TRIANGLES)

                x = (col+1) - (self.cols/2)
                y = (row+1) - (self.rows/2)
                z = self.M[row+1][col+1]

                color = z*(0.7/8) + 0.3
                glColor3f(color, color, color)
                glVertex3f(x, y, -z)

                x = col     - (self.cols/2)
                y = (row+1) - (self.rows/2)
                z = self.M[row+1][col]

                color = z*(0.7/8) + 0.3
                glColor3f(color, color, color)
                glVertex3f(x, y, -z)

                x = (col+1) - (self.cols/2)
                y = row     - (self.rows/2)
                z = self.M[row][col+1]

                color = z*(0.7/8) + 0.3
                glColor3f(color, color, color)
                glVertex3f(x, y, -z)

                glEnd()

        #end drawing

        glPopMatrix()

        glutSwapBuffers()
        #glFlush()

if __name__ == '__main__':
    myProgram = Scene()
