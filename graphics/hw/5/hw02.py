from graphics import *

planepoint = Point3D(2,4,2)
planenormal = Normal(-3,-3,-2)

planepoint = -planepoint

plane = planenormal * planepoint

print (type(plane))

o = Point3D(1,1,-10)
d = Vector3D(2,2,4)

camera = Ray(o,d)
