#!/usr/bin/python3

# Load in Required libraries
import numpy, time, sys
from Particle import *

sys.dont_write_bytecode = True

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

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
        tht = numpy.arccos((p1.dot(p2))/(numpy.linalg.norm(p2) * numpy.linalg.norm(p1)))
        # Calculate the axis of rotation (u)
        u = (numpy.cross(p1, p2) / (numpy.linalg.norm(p2) * numpy.linalg.norm(p1)))
        return tht, u

    # Scene Initialization
    def __init__(self):
        self.width = 400
        self.height = 400
        self.camera = 150

        self.particles = []

        for i in range(0, 10000):
            p = Particle(numpy.array([0.0, 0.0, 0.0]), numpy.array([0.0, -9.8, 0.0]), i)
            self.particles.append(p)

        self.last = time.time()
        self.timeStep = 0.01
        self.time = 0.0

        #rotation variables
        self.P1 = numpy.array([0,0,0])
        self.P2 = numpy.array([0,0,0])
        self.tht = 0.0
        self.u = numpy.array([0,0,0])
        self.wr = []

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Lab 11 - Part 1")
        glutDisplayFunc(self.display)
        glutIdleFunc(self.idle)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.keyboardSpecial)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 200.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glutMainLoop()

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
        tht, u = self.vector_angle(self.P1, self.P2)
        self.wr[-1] = [tht, u]
        glutPostRedisplay()

    def idle(self):
        if time.time() > self.last+self.timeStep:
            self.last = time.time()
            self.time += self.timeStep
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


        #lets draw!
        for part in self.particles:
            part.drawMe(self.time)

        # Lets put a cube in the middle!
        glColor3f(1.0, 1.0, 1.0)
        glutWireCube(20)

        glPopMatrix()
        glutSwapBuffers()

if __name__ == '__main__':
    myProgram = Scene()
