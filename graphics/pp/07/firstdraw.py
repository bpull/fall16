#!/usr/bin/python3

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# The function that we will use to draw the environment
def display():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glColor3f(1.0, 1.0, 1.0)   # White

    glBegin(GL_TRIANGLE_FAN)
    glColor3f(1.0, 1.0, 1.0)
    glVertex3f(100.0,100.0,0.0)
    glColor3f(0.0, 0.5, 0.5)
    glVertex3f(100.0,110.0,0.0)
    glColor3f(1.0, 0.0, 0.1)
    glVertex3f(110.0,110.0,0.0)
    glColor3f(0.5, 0.0, 0.5)
    glVertex3f(117.0,100.0,0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f(110.0, 90.0,0.0)
    glColor3f(0.5, 0.5, 0.0)
    glVertex3f(100.0, 90.0,0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex3f( 90.0, 90.0,0.0)
    glColor3f(1.0, 0.0, 0.0)
    glVertex3f( 83.0,100.0,0.0)
    glColor3f(0.0, 0.7, 0.8)
    glVertex3f( 90.0,110.0,0.0)
    glColor3f(0.0, 0.5, 0.5)
    glVertex3f(100.0,110.0,0.0)
    glEnd()

    glFlush()

# Initialize the environment
glutInit(sys.argv)
glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)

# Set the initial window position and size (if we want to)
glutInitWindowPosition(100,50)
glutInitWindowSize(400, 400)

# Create the window and name it
glutCreateWindow("ex1.py")

# Build the scene
glutDisplayFunc(display)

# Build the Bounding box - much more on this later!
glOrtho(50.0, 150.0, 50.0, 150.0, -10.0, 1.0)

# Go into a loop
glutMainLoop()
