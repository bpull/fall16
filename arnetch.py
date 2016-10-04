#!/usr/bin/python3

"""
Nick Arnold - 170252
Lab 04: part 1
"""
# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from math import *

class Scene:
    def __init__(self, *args):
        #create list to store points
        if flag == "-l":
            self.points_arr = myFile.read()
            self.points_arr = eval(self.points_arr)
        else:
            self.points_arr = []

        self.color = 'W'

        # Initialize the environment and display
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowPosition(1000,100)
        glutInitWindowSize(600, 500)
        glutCreateWindow("Lab 4 - Etch-a-Sketch")
        glutDisplayFunc(self.display)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.keyboardSpecial)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glOrtho(0.0, 600.0, 0.0, 500.0, -2.0, 1.0)
        glutMainLoop()

    # The function that we will use to draw the environment
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        if self.color is 'W':
            glColor3f(1.0, 1.0, 1.0)   #white
        if self.color is 'R':
            glColor3f(1.0, 0.0, 0.0)   #red
        if self.color is 'G':
            glColor3f(0.0, 1.0, 0.0)   #green
        if self.color is 'B':
            glColor3f(0.0, 0.0, 1.0)   #blue

        #draw text
        glRasterPos3f(220, 470, 0)
        title = "Etch A Sketch"
        for charachter in title:
            glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(charachter))

        # draw circle 1
        verts = 30
        glBegin(GL_POLYGON)
        for i in range(verts):
            x = 40*cos((2*i*pi)/verts)+50
            y = 40*sin((2*i*pi)/verts)+50
            glVertex2f(x,y)
        glEnd()

        # draw circle 2
        glBegin(GL_POLYGON)
        for i in range(verts):
            x = 40*cos((2*i*pi)/verts)+550
            y = 40*sin((2*i*pi)/verts)+50
            glVertex2f(x,y)
        glEnd()

        # draw hollow box
        glBegin(GL_LINE_LOOP)
        glVertex3i(100,100,0)
        glVertex3i(100,450,0)
        glVertex3i(500,450,0)
        glVertex3i(500,100,0)
        glEnd()

        #print drawing
        glPointSize(3.0)
        for point in self.points_arr:
            glBegin(GL_POINTS)
            glVertex(point[0],point[1],0)
            glEnd()

        #print image
        glFlush()

    # handles key presses with key as charachter of press
    def keyboard(self, key, col, row):
        print ("keyboard", key, col, row)

        #quit
        if key is 'q':
            print ("\nSystem Closing\n")

            if flag == "-s":
                myFile.write(str(self.points_arr)+'\n\n')

            sys.exit(1)

        #print saved points
        if key is 'p':
            print (self.points_arr)

        #clear screen
        if key is 'c':
            self.points_arr = []

        #change colors
        if key is 'W':
            self.color = 'W'
        if key is 'R':
            self.color = 'R'
        if key is 'G':
            self.color = 'G'
        if key is 'B':
            self.color = 'B'

        glutPostRedisplay()

    # handles key presses with key as ascii value of press
    def keyboardSpecial(self, key, col, row):
        print ("keyboardSpecial", key, col, row)
        glutPostRedisplay()

    # handles mouse clicks in window
    def mouse(self, buttonNumber, state, col, row):
        print ("mouse", buttonNumber, state, col, row)
        glutPostRedisplay()

    # handles mouse movement in window
    def motion(self, col, row):
        print ("motion", col, row)

        #prohibit off-screen drawing
        if (col>100 and col<500) and (row>50 and row<400):
            self.storePoints(col, 500-row)

        glutPostRedisplay()

    # stores points and line segments to print
    def storePoints(self, col, row):
        point = [col,row]
        self.points_arr.append(point)

#accept arguments
flag = None
if len(sys.argv) == 3:
    flag = sys.argv[1]
    if flag == "-s":
        myFile = open(sys.argv[2], 'w')
    elif flag == "-l":
        myFile = open(sys.argv[2], 'r')
    else:
        print("\nUSAGE: -s <file> to save or -l <file> to load\n")
        sys.exit(1)


#create the Scene
s = Scene(flag)
