#!/usr/bin/python3

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import objects
import time

def box(deltaX, deltaY, scale, lx, ly, ux, uy, Z, fill=False):
    glBegin(GL_LINE_LOOP)
    glVertex3f(scale*(deltaX+lx),scale*(deltaY+ly),Z)
    glVertex3f(scale*(deltaX+ux),scale*(deltaY+ly),Z)
    glVertex3f(scale*(deltaX+ux),scale*(deltaY+uy),Z)
    glVertex3f(scale*(deltaX+lx),scale*(deltaY+uy),Z)
    glEnd()

def text(deltaX, deltaY, scale, start_row, start_col, start_z, font, word):
    glRasterPos3f(scale*(deltaX+start_row), scale*(deltaY+start_col), start_z)
    for char in word:
        glutBitmapCharacter(font, ord(char))

#drange definition taken from http://stackoverflow.com/questions/477486/python-decimal-range-step-value
def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step
#end citation

def circle(deltaX, deltaY, scale, x, y, z, r, numberOfVertices, fill=False):
    if fill:
        glBegin(GL_TRIANGLE_FAN)
        glVertex3f(X, Y, 0.0)
    else:
        glBegin(GL_LINE_LOOP)
    theta=0
    for i in range(numberOfVertices):
        glVertex3f(scale*(deltaX+x)+math.cos(theta)*(r*scale),scale*(deltaY+y)+math.sin(theta)*(r*scale), z*scale)
        theta = theta + 2*math.pi / numberOfVertices
    glEnd()

def line(deltaX, deltaY, scale, x1, y1, x2, y2, Z):
    glBegin(GL_LINES)
    glVertex3f(scale*(deltaX+x1), scale*(deltaY+y1), Z)
    glVertex3f(scale*(deltaX+x2), scale*(deltaY+y2), Z)
    glEnd()

def color(deltaX, deltaY, scale, r, g, b):
    glColor3f(r, g, b)

class Scene:

    def keyboard(self, key, x, y):
        print ("['key', "+str(key)+", "+str(x)+", "+str(y)+"]")
        if key == 'w' or key == 'a' or key == 's' or key == 'd':
            if key == 'w':
                self.dir = "front"
                self.deltaYman += self.stepSize
            elif key == 's':
                self.dir = "front"
                self.deltaYman -= self.stepSize
            elif key == 'd':
                self.dir = "right"
                self.deltaXman += self.stepSize
            elif key == 'a':
                self.dir = "left"
                self.deltaXman -= self.stepSize
            self.stage = (self.stage + 1) % 3

        if str(key) is 'q':
            glutDestroyWindow(1)
        else:
            glutPostRedisplay()

    def keyboardSpecial(self, key, x, y):
        print ("['key special', "+str(key)+", "+str(x)+", "+str(y)+"]")

        if key == 101:
            self.dir = "front"
            if self.deltaYman < 450:
                self.deltaYman += self.stepSize
        elif key == 103:
            self.dir = "front"
            if self.deltaYman > -75:
                self.deltaYman -= self.stepSize
        elif key == 102:
            self.dir = "right"
            if self.deltaXman < 550:
                self.deltaXman += self.stepSize
        elif key == 100:
            self.dir = "left"
            if self.deltaXman > -50:
                self.deltaXman -= self.stepSize
        self.stage = (self.stage + 1) % 3

        glutPostRedisplay()

    def mouse(self, button, state, x, y):
        print ("['mouse', "+str(button)+", "+str(state)+", "+str(x)+", "+str(y)+"]")
        if str(button) is '3' and str(state) is '0':
            if self.scaleman < 2:
                self.scaleman += 0.25
                if self.stepSize < 20:
                    self.stepSize *= 1.2
        elif str(button) is '4' and str(state) is '0':
            if self.scaleman > .5:
                self.scaleman -= 0.25
                if self.stepSize > 4:
                    self.stepSize /= 1.2
        glutPostRedisplay()

    def motion(self, x, y):
        print ("['motion', "+str(x)+", "+str(y)+"]")
        glutPostRedisplay()

    def idle(self):
        if (time.time() / 0.2) % 1 == 0:
            print ("['time', "+str(time.time())+"]")
            if self.dir == "front":
                self.stage = (self.stage + 1) % 3
                glutPostRedisplay()

    def __init__(self):

        self.window_height = 500
        self.dir = "front"
        self.stage = 0
        self.deltaXman = 100
        self.deltaYman = 100
        self.scaleman = 1.0
        self.stepSize = 4;


        # Initialize the environment
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)


        # Set the initial window position and size (if we want to)
        glutInitWindowSize(600, 500)

        # Create the window and name it
        glutCreateWindow("Lab 5 - Animation")

        # Build the scene
        glutDisplayFunc(self.display)

        # Build the Bounding box - much more on this later!
        glOrtho(0.0, 600.0, 0.0, 500.0, -2.0, 1.0)

        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.keyboardSpecial)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glutIdleFunc(self.idle)

        # Go into a loop
        glutMainLoop()

    # The function that we will use to draw the environment
    def display(self):

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        box(0, 0, 1.0, 25, 25, 575, 450, 0)
        text(0, 0, 1.0, 190, 470, 0, GLUT_BITMAP_TIMES_ROMAN_24, "Our Game Experience")

        for component in objects.stickFigure[self.dir][self.stage]:
            component[0](self.deltaXman,self.deltaYman,self.scaleman,*component[1])

        glFlush()

if __name__ == '__main__':
    game = Scene()
