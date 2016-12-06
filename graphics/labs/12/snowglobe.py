#!/usr/bin/python3

# Load in Required libraries
import numpy, time, sys
from snow import *

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
        self.width = 800
        self.height = 800
        self.camera = 100

        self.particles = []

        for i in range(0, 500):
            startx = numpy.random.uniform(-35.0,35.0)
            startz = numpy.random.uniform(-35.0,35.0)
            p = Particle(numpy.array([startx, 60.0, startz]), numpy.array([0.0, -9.8, 0.0]), i)
            self.particles.append(p)

        self.last = time.time()
        self.timeStep = 0.01
        self.time = 0.0

        self.radius = 70.0
        self.stepSizeX = 10
        self.stepSizeY = 10

        #rotation variables
        self.P1 = numpy.array([0,0,0])
        self.P2 = numpy.array([0,0,0])
        self.tht = 0.0
        self.u = numpy.array([0,0,0])
        self.wr = []

        glutInit(sys.argv)
        glutInitDisplayMode(GLUT_DOUBLE|GLUT_RGB|GLUT_DEPTH)
        glutInitWindowSize(self.width, self.height)
        glutCreateWindow("Snow Globe")
        glutDisplayFunc(self.display)
        glutIdleFunc(self.idle)
        glutKeyboardFunc(self.keyboard)
        glutSpecialFunc(self.keyboardSpecial)
        glutMouseFunc(self.mouse)
        glutMotionFunc(self.motion)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glFrustum(-5.0, 5.0, -5.0, 5.0, 5.0, 250.0)
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glEnable(GL_DEPTH_TEST)
        glutMainLoop()

    # hit a key
    def keyboard(self, key, x, y):
        if str(key) == 'q' or str(key) == '\x1b':
            sys.exit(1)

    # hit a special key
    def keyboardSpecial(self, key, x, y):
        if key == 104:
            if self.stepSizeX > 1:
                self.stepSizeX -= 1
            if self.stepSizeY > 1:
                self.stepSizeY -= 1
        elif key == 105:
            if self.stepSizeX <= 180:
                self.stepSizeX += 1
            if self.stepSizeY <= 180:
                self.stepSizeY += 1
        #glutPostRedisplay()

    # Click the mouse
    def mouse(self, button, state, x, y):
        if button == 3:
            self.camera -= 2
        elif button == 4:
            self.camera += 2
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

    def circle(self, x, y, z, r,):
        glBegin(GL_LINE_LOOP)
        theta=0
        for i in range(30):
            glVertex3f(x+math.cos(theta)*r, y, z+math.sin(theta)*r)
            theta = theta + 2*math.pi / 30
        glEnd()


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

        #snowglobe base
        self.circle(0.0, -40.0, 0.0, 50.0)
        self.circle(0.0, -45.0, 0.0, 60.0)


        #snowglobe glass
        glBegin(GL_POINTS)
        for angleX in range(0,360,self.stepSizeX):
            for angleY in range(0, 360, self.stepSizeY):
                radX = angleX * math.pi / 180
                radY = angleY * math.pi / 180
                z = self.radius*math.cos(radX)*math.sin(radY)
                y = self.radius*math.sin(radX)*math.sin(radY)
                x = self.radius*math.cos(radY)
                if y > -42:
                    glVertex3f(x,y,z)
        glEnd()


        #snow
        for part in self.particles:
            part.drawMe(self.time)

        #ornaments
        glColor(0,0,1)

        glTranslatef(15,9,3)
        glutSolidSphere(2.5,20,20)
        glTranslatef(-15,-9,-3)

        glColor(1,1,0)

        glTranslatef(3,-20,15)
        glutSolidSphere(2.5,20,20)
        glTranslatef(-3,20,-15)

        glColor(1,0,0)

        glTranslatef(-8,-5,0)
        glutSolidSphere(2.5,20,20)
        glTranslatef(8,5,0)

        #leaves
        glColor(.302,.620,.227)

        glTranslatef(10.0,22,-10.0)
        glRotate(-90,1,0,0)
        glutSolidCone(10.0,22,40,40)
        glRotate(90,1,0,0)
        glTranslatef(-10.0,-22,10.0)

        glTranslatef(10.0,12,-10.0)
        glRotate(-90,1,0,0)
        glutSolidCone(13.0,25,40,40)
        glRotate(90,1,0,0)
        glTranslatef(-10.0,-12,10.0)

        glTranslatef(10.0,1,-10.0)
        glRotate(-90,1,0,0)
        glutSolidCone(19.0,25,40,40)
        glRotate(90,1,0,0)
        glTranslatef(-10.0,-1,10.0)

        glTranslatef(10.0,-11.0,-10.0)
        glRotate(-90,1,0,0)
        glutSolidCone(25.0,30,40,40)
        glRotate(90,1,0,0)
        glTranslatef(-10.0,11.0,10.0)

        glTranslatef(10.0,-25.0,-10.0)
        glRotate(-90,1,0,0)
        glutSolidCone(30.0,30,40,40)
        glRotate(90,1,0,0)
        glTranslatef(-10.0,25.0,10.0)

        # tree base
        glColor3f(.369,.149,.071)
        glTranslatef(10.0,-40.0,-10.0)
        glRotate(-90,1,0,0)
        glutSolidCone(8.0,70,40,40)
        glRotate(90,1,0,0)
        glTranslatef(-10.0,40.0,10.0)
        glTranslatef(10.0,-20.0,-10.0)


        #snowman nose
        glColor3f(1.0,0.5,0.0)
        glTranslatef(-24.5,7,44)
        glutSolidCone(1.0,3,20,20)
        glTranslatef(24.5,-7,-44)


        #snowman eyes
        glColor3f(0.0,0.0,0.0)
        glTranslatef(-26,9,44)
        glutSolidSphere(1.0,20,20)
        glTranslatef(26,-9,-44)
        glTranslatef(-23,9,44)
        glutSolidSphere(1.0,20,20)
        glTranslatef(23,-9,-44)

        #snowman body
        glColor3f(1.0,1.0,1.0)
        glTranslatef(-25,-12,40)
        glutSolidSphere(8.0,20,20)
        glTranslatef(25,12,-40)

        glTranslatef(-25,-1,40)
        glutSolidSphere(6.0,20,20)
        glTranslatef(25,1,-40)

        glTranslatef(-25,8,40)
        glutSolidSphere(4.0,20,20)
        glTranslatef(25,-8,-40)



        glPopMatrix()
        glutSwapBuffers()

if __name__ == '__main__':
    myProgram = Scene()
