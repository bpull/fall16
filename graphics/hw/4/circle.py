#!/usr/bin/python3

# Our required libraries!
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def createCircle(cx, cy, rad, verts):
    theta = 360/verts
    count = 1
    firstx = (cx + rad * math.cos(theta))
    firsty = (cy + rad * math.sin(theta))

    while theta < 360:
        theta = (360/verts) * count
        x = (cx + rad * math.cos(theta))
        y = (cy + rad * math.sin(theta))
        print ("["+str(x)+","+str(y)+"]")
        glVertex3f(x, y, 0.0)
        count = count + 1

    glVertex3f(firstx, firsty, 0.0)

# The function that we will use to draw the environment
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)   # White

    glBegin(GL_LINE_LOOP)
    createCircle(50, 50, 25, 10) #last parameter is the number of vertices
    glEnd()

    glFlush()

# Initialize the environment
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)

# Set the initial window position and size (if we want to)
glutInitWindowPosition(100,50)
glutInitWindowSize(400, 400)

# Create the window and name it
glutCreateWindow("Brandon Pullig 175148")

# Build the scene
glutDisplayFunc(display)

# Build the Bounding box - much more on this later!
glOrtho(0.0, 100.0, 0.0, 100.0, -2.0, 1.0)

# Go into a loop
glutMainLoop()
