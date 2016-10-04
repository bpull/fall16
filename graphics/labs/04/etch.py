#!/usr/bin/python3

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import math
import csv

class Scene:

    def keyboard(self, key, x, y):
        print ("['key', "+str(key)+", "+str(x)+", "+str(y)+"]")
        if str(key) is 'q':
            glutDestroyWindow(1)
        elif str(key) is 'c':
            self.line = []
            self.lines = []
            self.points = []
            glutPostRedisplay()
        else:
            glutPostRedisplay()

    def keyboardSpecial(self, key, x, y):
        print ("['key special', "+str(key)+", "+str(x)+", "+str(y)+"]")
        glutPostRedisplay()

    def mouse(self, buttonNumber, state, x, y):
        print ("['mouse', "+str(buttonNumber)+", "+str(state)+", "+str(x)+", "+str(y)+"]")
        if str(buttonNumber) is '0' and str(state) is '0':
            if len(self.line) is 1:
                self.points.append(self.line[0])
            self.lines.append(self.line)
            self.line = []
        elif str(buttonNumber) is '0' and str(state) is '1':
            if 100 < x and x < 500 and 100 < self.window_height-y and self.window_height-y < 450:
                self.points.append([x,self.window_height-y])
        elif str(buttonNumber) is '3' and str(state) is '0':
            if self.line_width < 9:
                self.line_width += 1
        elif str(buttonNumber) is '4' and str(state) is '0':
            if self.line_width > 1:
                self.line_width -= 1
        glutPostRedisplay()

    def motion(self, x, y):
        print ("['motion', "+str(x)+", "+str(y)+"]")
        if 100 < x and x < 500 and 100 < self.window_height-y and self.window_height-y < 450:
            self.line.append([x,self.window_height-y])
        glutPostRedisplay()

    def __init__(self):

        self.line_width = 2
        self.window_height = 500
        self.line = []
        self.lines = []
        self.points = []

        # Initialize the environment
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)

        # Set the initial window position and size (if we want to)
        glutInitWindowSize(600, 500)

        # Create the window and name it
        glutCreateWindow("Lab 4 - Etch-a-Sketch")

        # Build the scene
        glutDisplayFunc(self.display)

        # Build the Bounding box - much more on this later!
        glOrtho(0.0, 600.0, 0.0, 500.0, -2.0, 1.0)

        # Go into a loop
        glutMainLoop()

    def draw_box(self, llx,lly,urx,ury):
        glBegin(GL_LINE_LOOP)
        glVertex3f(100,100,0)
        glVertex3f(500,100,0)
        glVertex3f(500,450,0)
        glVertex3f(100,450,0)
        glEnd()

    def write_word(self, word, start_row, start_col, start_z):
        glRasterPos3f(start_row, start_col, start_z)
        for char in word:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))

    def draw_circle(self, x, y, z, r):
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_POLYGON)
        for i in range(360):
            i = i*math.pi/180
            glVertex3f(x+math.cos(i)*r,y+math.sin(i)*r, z)
        glEnd()

    # The function that we will use to draw the environment
    def display(self):
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.keyboardSpecial)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)


        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glColor3f(1.0, 1.0, 1.0)   # White

        glLineWidth(2.0)
        self.draw_box(100,100,500,450)
        self.write_word("Etch A Sketch", 220, 470, 0)
        self.draw_circle(50,50,0,40)
        self.draw_circle(550,50,0,40)

        glLineWidth(self.line_width)
        glColor3f(1.0, 1.0, 1.0)   # White
        glBegin(GL_POINTS)
        for point in self.points:
            glVertex3f(point[0], point[1],0)
        glEnd()

        glBegin(GL_LINE_STRIP)
        for point in self.line:
            glVertex3f(point[0], point[1], 0)
        glEnd()

        glColor3f(1.0, 1.0, 1.0)   # White
        for line_seg in self.lines:
            glBegin(GL_LINE_STRIP)
            for point in line_seg:
                glVertex3f(point[0], point[1], 0)
            glEnd()


        glFlush()

etch = Scene()
