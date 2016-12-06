#!/usr/bin/python3

# Load in Required libraries
import numpy, math, time, random

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from particle import *
# Our new Scene Class
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



    # Scene Initialization
    def __init__(self):
        self.width = 400
        self.height = 400
        self.camera = 60

        self.P1 = numpy.array([0,0,0])
        self.P2 = numpy.array([0,0,0])
        self.theta = 0.0
        self.u = numpy.array([0,0,0])
        self.wr = []
        self.track = time.time()
        self.trackStep = 0.02
        self.timeStep = 0.01
        self.Time = 0.0
        self.particles = []

        for i in range(0, 10000):
            p = particle(numpy.array([0.0, 0.0, 0.0]), numpy.array([0.0, 0.0, 0.0]), numpy.array([0.0, -9.8, 0.0]), i)
            self.particles.append(p)

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Lab 11")
        glutDisplayFunc(self.display)
        glutIdleFunc(self.idle)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.keyboardSpecial)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glutMainLoop()


    def idle(self):
        if (time.time() - self.track) > self.trackStep:
            self.track = time.time()
            self.Time += self.timeStep
            glutPostRedisplay()

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



        glColor3f(1.0, 1.0, 1.0)
        glutWireCube(20)

        for i in range(0, 10000):
            self.particles[i].draw(self.Time)

        glPopMatrix()
        glutSwapBuffers()

if __name__ == '__main__':
    myProgram = Scene()
