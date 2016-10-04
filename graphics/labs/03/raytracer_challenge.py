from graphics import *
from ppm import PPM
from raytracer_part3 import raytracer

# Build the Spheres that will be in our world
S1 = Sphere(Point3D(300,200,200), 100, ColorRGB(1.0,0.2,0.4))
S2 = Sphere(Point3D(-200,-100,50), 35, ColorRGB(0.3,0.8,0.2))
S3 = Sphere(Point3D(50,20,100), 25, ColorRGB(0.4,0.1,0.4))
S4 = Sphere(Point3D(300,-200,600), 250, ColorRGB(0.6,0.6,0.4))
S5 = Sphere(Point3D(400,400,900), 400, ColorRGB(0.0,0.2,1.0))

# Build the Planes that will be in our world
P1 = Plane(Point3D(50,50,999), Normal(0,0,1), ColorRGB(0.8,0.8,0.8))
P2 = Plane(Point3D(50,50,900), Normal(1,1,1), ColorRGB(1.0,1.0,1.0))

vp = ViewPlane(Point3D(0,0,0), Normal(0,0,1), 640, 480, 1.0)
Camera1 = Ray(Point3D(0,0,-100), Normal(0,0,1))

objects = []
objects.append(S1)
objects.append(S2)
objects.append(S3)
objects.append(S4)
objects.append(S5)
objects.append(P1)
objects.append(P2)

rt = raytracer(vp, objects)
rt.color_plane_challenge(Camera1)
camera = rt.get_viewplane()

PPM(camera, 'part5_1.ppm')
