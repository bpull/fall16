from graphics import *

a = Point3D(2,4,2)
n = Normal(-3,-3,-2)

o = Point3D(1,1,-10)
d = Vector3D(2,2,4)

camera = Ray(o,d)

t = ((a - o) * n) / (d * n)

p = o + (d * t)
print (p)

#answer is [ 4.6  4.6 -2.8]

#The reason we did (d*t) instead of (t*d) is because
#the vector must be multiplied with the float. It is how the
#function is written in graphics.py. There is no function
#for float*vector3d
