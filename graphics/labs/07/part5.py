#!/usr/bin/python3

# Load in Required libraries
import math, numpy, time
import PIL.Image as Image

# Our required libraries!
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# Our new Scene Class
class Scene:
    def keyboardSpecial(self, key, x, y):
        if key == 101:
            self.up += .3
        elif key == 103:
            self.up -= .3
        elif key == 102:
            self.angle += .07
        elif key == 100:
            self.angle -= .07

        glutPostRedisplay()

    def __init__(self):
        self.width = 400
        self.height = 400
        self.timeStep = 0
        self.timeStepSize = 0.02
        self.angle = 0.0
        self.length = 5.0
        self.up = 0.5
        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        #glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowPosition(100,50)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Part 5")
        glutDisplayFunc(self.display)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 100.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)

        # New lines for images/textures
        glShadeModel( GL_SMOOTH )
        glEnable( GL_TEXTURE_2D )

        #Load Image 1
        im = Image.open(sys.argv[-1])
        self.xSize = im.size[0]
        self.ySize = im.size[1]
        self.rawReference = im.tobytes("raw", "RGB", 0, -1)

        glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT )
        glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT )
        glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR )
        glTexParameterf( GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR )
        glTexImage2D( GL_TEXTURE_2D, 0, 3, self.xSize, self.ySize, 0,
             GL_RGB, GL_UNSIGNED_BYTE, self.rawReference )
        glGenerateMipmap(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D,0)

        glutSpecialFunc(self.keyboardSpecial)

        glutMainLoop()

    # Build the scene
    def display(self):
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        #cube framework
        glPushMatrix()
        glColor3f(1.0, 0.0, 0.0)
        gluLookAt(10*math.cos(self.angle), self.up, 10*math.sin(self.angle), 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)
        glutWireCube(self.length)

        ############begin front face##############

        glColor3f(1,1,1)
        glBegin(GL_TRIANGLES)
        glTexCoord2f(0,1)
        glVertex3f(-2.5, 2.5, -2.5)
        glTexCoord2f(0,0)
        glVertex3f(-2.5, -2.5, -2.5)
        glTexCoord2f(1,0)
        glVertex3f(2.5, -2.5, -2.5)
        glEnd()


        glColor3f(1,1,1)
        glBegin(GL_TRIANGLES)
        glTexCoord2f(0,1)
        glVertex3f(-2.5, 2.5, -2.5)
        glTexCoord2f(1,1)
        glVertex3f(2.5, 2.5, -2.5)
        glTexCoord2f(1,0)
        glVertex3f(2.5, -2.5, -2.5)
        glEnd()


        # ############begin right face##############

        glBegin(GL_TRIANGLES)
        glColor3f(1,1,1)
        glVertex3f(2.5, 2.5, -2.5)
        glColor3f(1,1,0)
        glVertex3f(2.5, -2.5, -2.5)
        glColor3f(0,1,0)
        glVertex3f(2.5, -2.5, 2.5)
        glEnd()


        glBegin(GL_TRIANGLES)
        glColor3f(1,1,1)
        glVertex3f(2.5, 2.5, -2.5)
        glColor3f(0,1,1)
        glVertex3f(2.5, 2.5, 2.5)
        glColor3f(0,1,0)
        glVertex3f(2.5, -2.5, 2.5)
        glEnd()


        # ############begin back face##############

        glBegin(GL_TRIANGLES)
        glColor3f(0,1,1)
        glVertex3f(2.5, 2.5, 2.5)
        glColor3f(0,0,0)
        glVertex3f(-2.5, -2.5, 2.5)
        glColor3f(0,0,1)
        glVertex3f(-2.5, 2.5, 2.5)
        glEnd()


        glBegin(GL_TRIANGLES)
        glColor3f(0,1,1)
        glVertex3f(2.5, 2.5, 2.5)
        glColor3f(0,0,0)
        glVertex3f(-2.5, -2.5, 2.5)
        glColor3f(0,1,0)
        glVertex3f(2.5, -2.5, 2.5)
        glEnd()


        # ############begin left face##############

        glBegin(GL_TRIANGLES)
        glColor3f(0,0,1)
        glVertex3f(-2.5, 2.5, 2.5)
        glColor3f(0,0,0)
        glVertex3f(-2.5, -2.5, 2.5)
        glColor3f(1,0,0)
        glVertex3f(-2.5, -2.5, -2.5)
        glEnd()


        glBegin(GL_TRIANGLES)
        glColor3f(0,0,1)
        glVertex3f(-2.5, 2.5, 2.5)
        glColor3f(1,0,1)
        glVertex3f(-2.5, 2.5, -2.5)
        glColor3f(1,0,0)
        glVertex3f(-2.5, -2.5, -2.5)
        glEnd()


        # ############begin top face##############

        glBegin(GL_TRIANGLES)
        glColor3f(1,1,1)
        glVertex3f(2.5, 2.5, -2.5)
        glColor3f(1,0,1)
        glVertex3f(-2.5, 2.5, -2.5)
        glColor3f(0,0,1)
        glVertex3f(-2.5, 2.5, 2.5)
        glEnd()


        glBegin(GL_TRIANGLES)
        glColor3f(0,0,1)
        glVertex3f(-2.5, 2.5, 2.5)
        glColor3f(0,1,1)
        glVertex3f(2.5, 2.5, 2.5)
        glColor3f(1,1,1)
        glVertex3f(2.5, 2.5, -2.5)
        glEnd()


        # ############begin bottom face##############

        glBegin(GL_TRIANGLES)
        glColor3f(1,1,0)
        glVertex3f(2.5, -2.5, -2.5)
        glColor3f(1,0,0)
        glVertex3f(-2.5, -2.5, -2.5)
        glColor3f(0,0,0)
        glVertex3f(-2.5, -2.5, 2.5)
        glEnd()


        glBegin(GL_TRIANGLES)
        glColor3f(1,1,0)
        glVertex3f(2.5, -2.5, -2.5)
        glColor3f(0,1,0)
        glVertex3f(2.5, -2.5, 2.5)
        glColor3f(0,0,0)
        glVertex3f(-2.5, -2.5, 2.5)
        glEnd()



        glPopMatrix()

        glutSwapBuffers()
        #glFlush()

if __name__ == '__main__':
    myProgram = Scene()
