#!/usr/bin/python3

# Our required libraries!
import math
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

#drange definition taken from http://stackoverflow.com/questions/477486/python-decimal-range-step-value
def drange(start, stop, step):
    r = start
    while r < stop:
        yield r
        r += step
#end citation

def createCircle(cx, cy, rad, verts):

    spread = 360.0 / verts
    for i in drange(0, 360, spread):
        i = i*math.pi/180
        glVertex3f(cx+math.cos(i)*rad,cy+math.sin(i)*rad, 0.0)

# The function that we will use to draw the environment
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)   # White

    glBegin(GL_LINE_LOOP)
    createCircle(50, 50, 25, 50) #last parameter is the number of vertices
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
