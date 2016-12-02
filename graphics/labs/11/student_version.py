#!/usr/bin/python3

# Load in Required libraries
import numpy

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

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Arcball Demo")
        glutDisplayFunc(self.display)
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

        # Lets make a sphere!
        glColor3f(1.0,1.0,1.0)
        radius = 30.0
        phi = 0.0
        for theta in range(0, 360, 10):
            glBegin(GL_POINTS)
            for t in range(0, 360, 10):
                n = numpy.array([numpy.cos(numpy.radians(phi))*numpy.sin(numpy.radians(theta)),
                                 numpy.sin(numpy.radians(theta))*numpy.sin(numpy.radians(phi)),
                                 numpy.cos(numpy.radians(theta))])
                u = numpy.array([-numpy.sin(numpy.radians(phi)),
                                 numpy.cos(numpy.radians(phi)),
                                 0.0])
                C = numpy.array([0.0, 0.0, 0.0])
                P = radius * numpy.cos(numpy.radians(t))*u + radius * numpy.sin(numpy.radians(t)) * (numpy.cross(n,u)) + C
                glVertex3f(P[0], P[1], P[2])
            glEnd()

        # Lets put a cube in the middle!
        glColor3f(1.0, 1.0, 1.0)
        glutWireCube(20)

        glPopMatrix()
        glutSwapBuffers()

if __name__ == '__main__':
    myProgram = Scene()
