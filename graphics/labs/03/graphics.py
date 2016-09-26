# B.S. Pulllig (m175148)
#Code from import numpy to the end of Sphere Class is from LCDR Kenney
import numpy

# Vector3D Class
class Vector3D:
    def __init__(self, val, *args):
        if type(val) is numpy.ndarray:
            self.v = val
        elif args and len(args) == 2:
            self.v = numpy.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Vector3D")
    def __repr__(self):
        return str(self.v)
    def __add__(self, other):
        if isinstance(other, Point3D):
            return Point3D(self.v + other.v)
        elif isinstance(other, Normal):
            return Vector3D(self.v + other.v)
        else:
            return Vector3D(self.v + other.v)
    def __sub__(self, other):
        return Vector3D(self.v - other.v)
    def __div__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.v / other.v)
        else:
            return Vector3D(self.v / other)
    def __truediv__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.v / other.v)
        else:
            return Vector3D(self.v / other)
    def magnitude(self):
        return numpy.linalg.norm(self.v)
    def square(self):
        return numpy.square(self.mangitude())
    def __mul__(self, other):
        if isinstance(other, Vector3D) or isinstance(other, Normal):
            return numpy.dot(self.v, other.v)
        else:
            return Vector3D(self.v * other)
    def dot(self, other):
        if isinstance(other, Vector3D) or isinstance(other, Normal):
            return numpy.dot(self.v, other.v)
        else:
            raise Exception("You can only calc the dot product between a Normal and a Vector3D")
    def dotangle(self, other, angle):
        return self.magnitude() * other.magnitude() * numpy.cos(numpy.radians(angle))
    def cross(self, other):
        return Vector3D(numpy.cross(self.v, other.v))
    def copy(self):
        return Vector3D(self.v.copy())

# Point3D Class
class Point3D:
    def __init__(self, val, *args):
        if type(val) is numpy.ndarray:
            self.v = val
        elif args and len(args) == 2:
            self.v = numpy.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Point3D")
    def __repr__(self):
        return str(self.v)
    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Point3D(self.v + other.v)
        else:
            raise Exception("You can only add a Vector3D to a Point3D")
    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Point3D(self.v - other.v)
        elif isinstance(other, Point3D):
            return Vector3D(self.v - other.v)
        else:
            raise Exception("You can only subtract either a Vector3D or a Point3D from a Point3D")
    def __mul__(self, other):
        return Point3D(self.v * other)
    def distance(self, other):
        tmpVector = self.__sub__(other)
        return tmpVector.magnitude()
    def distancesquared(self, other):
        return numpy.square(self.distance(other))
    def copy(self):
        return Point3D(self.v.copy())

# Graphics Normal Class
class Normal:
    def __init__(self, val, *args):
        if type(val) is numpy.ndarray:
            self.v = val
        elif args and len(args) == 2:
            self.v = numpy.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Normal")
    def __repr__(self):
        return str(self.v)
    def copy(self):
        return Normal(self.v.copy())
    def __neg__(self):
        return Normal(self.v * -1)
    def __add__(self, other):
        if isinstance(other, Normal):
            return Normal(self.v + other.v)
        elif isinstance(other, Vector3D):
            return Vector3D(self.v + other.v)
        else:
            raise Exception("You can only add a Vector3D or a Normal to a Normal")
    def __mul__(self, other):
        if isinstance(other, Vector3D) or isinstance(other, Normal):
            return numpy.dot(self.v, other.v)
        else:
            return Normal(self.v * other)
    def dot(self, other):
        if isinstance(other, Vector3D):
            return numpy.dot(self.v, other.v)
        else:
            raise Exception("You can only calc the dot product between a Normal and a Vector3D")

# Ray Class
class Ray:
    def __init__(self, origin, direction):
        self.origin = origin
        self.direction = Vector3D(direction.v)
    def copy(self):
        return Ray(self.origin.copy(), self.direction.copy())
    def __repr__(self):
        return str([self.origin, self.direction])

# ColorRGB Class
class ColorRGB:
    def __init__(self, val, *args):
        if type(val) is numpy.ndarray:
            self.v = val
        elif args and len(args) == 2:
            self.v = numpy.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to ColorRGB")
    def __repr__(self):
        return str(self.v)
    def copy(self):
        return ColorRGB(self.v.copy())
    def get(self):
        return self.v[0], self.v[1], self.v[2]
    def __add__(self, other):
        return ColorRGB(self.v + other.v)
    def __mul__(self, other):
        if isinstance(other, ColorRGB):
            return ColorRGB(self.v * other.v)
        else:
            return ColorRGB(self.v * other)
    def __div__(self, other):
        return ColorRGB(self.v / other)
    def __truediv__(self, other):
        return ColorRGB(self.v / other)
    def __pow__(self, other):
        return ColorRGB(self.v ** other)

# Plane Class with Hit Point Detection
class Plane:
    def __init__(self, point, normal, color=ColorRGB(1,1,1)):
        self.point = point
        self.normal = normal
        self.color = color
    def copy(self):
        return Plane(self.point.copy(), self.normal.copy())
    def __repr__(self):
        return str([self.point, self.normal])
    def hit(self, ray, epsilon, shadeRec=False):
        t = ((self.point - ray.origin) * self.normal) / (ray.direction * self.normal)
        hit = ray.origin + ray.direction * t
        return True, t, hit, self.color

# Sphere Class with Hit Point Detection
class Sphere:
    def __init__(self, center, radius, color=ColorRGB(1,1,1)):
        self.center = center
        self.radius = radius
        self.color = color
    def copy(self):
        return Sphere(self.center.copy(), self.radius)
    def __repr__(self):
        return str([self.center, self.radius])
    def hit(self, ray, epsilon, shadeRec=False):
        a = ray.direction * ray.direction
        b = 2.0 * ((ray.origin - self.center) * ray.direction)
        c = (ray.origin - self.center) * (ray.origin - self.center) - self.radius**2
        d = b**2 - 4*a*c
        if d < 0:
            return False, False, False, False
        t1 = (-b + numpy.sqrt(d)) / (a*2)
        t2 = (-b - numpy.sqrt(d)) / (a*2)
        p1 = ray.origin + ray.direction*t1
        p2 = ray.origin + ray.direction*t2
        if max(t1,t2) < epsilon:
            return False, False, False, False
        if t1 > epsilon and t2 < epsilon:
            return True, t1, p1, self.color
        elif t2 > epsilon and t1 < epsilon:
            return True, t2, p2, self.color
        elif t1 < t2:
            return True, t1, p1, self.color
        else:
            return True, t2, p2, self.color


class ViewPlane:

    def __init__(self, center, normal, hres, vres, pixelsize):
        if isinstance(center, Point3D) and isinstance(normal, Normal):
            self.c = center
            self.n = normal
            self.hres = hres
            self.vres = vres
            self.pixelsize = pixelsize

            HxVres = []
            for i in range(vres):
                row = [ColorRGB(0.0,0.0,0.0)]*hres
                HxVres.append(row)
            self.hxr = HxVres
        else:
            raise Exception("Invalid arguments to ViewPlane")

    def get_color(self, row, col):
        return self.hxr[row][col]

    def set_color(self, row, col, color):
        if isinstance(color, ColorRGB):
            self.hxr[row][col] = color

    def get_point(self, row, col):
        Vup = Vector3D(0,-1,0)
        u = Vup.cross(-self.n)
        u = u / u.magnitude()
        v = u.cross(-self.n)
        LL = self.c - (u * (self.hres/2.0) * self.pixelsize) - (v * (self.vres/2.0) * self.pixelsize)
        return LL + u * (col+0.5) * self.pixelsize + v * (row+0.5) * self.pixelsize

    def get_resolution(self):
        return self.hres, self.vres

    def orthographic_ray(self, row, col):
        center = self.get_point(row, col)
        return Ray(center, self.n)

# We should always have debugging in our libraries
# that run if the file is called from the command line
# vice from an import statement!
def randomCube(fll, bur, n):
    '''takes 2 Point3Ds to define a cube and returns n random points inside the cube'''
    cube_points = []
    x_range = bur.p[0] - fll.p[0]
    y_range = bur.p[1] - fll.p[1]
    z_range = bur.p[2] - fll.p[2]

    for i in range(n):
        x = bur.p[0]-x_range*np.random.rand(1)
        y = bur.p[1]-y_range*np.random.rand(1)
        z = bur.p[2]-z_range*np.random.rand(1)
        rand_point = Point3D(float(x),float(y),float(z))
        cube_points.append(rand_point)
    return cube_points


if __name__ == '__main__':
    u = Vector3D(1,2,3)
    v = Vector3D(4,5,6)
    cint = float(10)

    print("Testing Printing...")
    if str(u) != '[ 1.  2.  3.]':
        raise Exception("Printing Error!")
    print("Testing Addition...")
    c = u + v
    if str(c) != '[ 5.  7.  9.]':
        raise Exception("Addition Error!")
    print("Testing Subtraction...")
    d = v - u
    if str(d) != '[ 3.  3.  3.]':
        raise Exception("Subtraction Error!")
    print("Testing Multiplication...")
    e = u * cint
    if str(e) != '[ 10.  20.  30.]':
        print (str(e))
        raise Exception("Multiplication Error!")
    print("Testing Division...")
    w = Vector3D(4,5,6)
    f = v / cint
    if str(f) != '[ 0.4  0.5  0.6]':
        print (str(f))
        raise Exception("Division Error!")
    print("Testing Equality...")
    g = u.copy()
    if str(g) != '[ 1.  2.  3.]':
        print (str(g))
        raise Exception("Equality Error!")
    print("Testing Magnitude...")
    x = Vector3D(1,2,2)
    h = x.magnitude()
    if h != 3:
        print (str(h))
        raise Exception("Magnitude Error!")
    print("Testing Square...")
    i = x.square()
    if i != 9:
        print (str(i))
        raise Exception("Square Error!")
    print("Testing Dot...")
    j = u.dot(v)
    if j != 32:
        print (str(j))
        raise Exception("Dot Error!")
    print("Testing Dot Angle...")
    k = x.dotangle(x,0)
    if k != 9:
        print (k)
        raise Exception("Dot Angle Error!")
    print("Testing Cross...")
    l = u.cross(v)
    if str(l) != '[-3.  6. -3.]':
        print (str(l))
        raise Exception("Cross Error!")
    print("Tests for Vector3D Complete!\n---------------")
    up = Point3D(1,2,3)
    vp = Point3D(4,5,6)
    print("Testing Printing...")
    if str(up) != '[ 1.  2.  3.]':
        raise Exception("Printing Error!")
    print("Testing Addition...")
    cp = up + v
    if str(cp) != '[ 5.  7.  9.]':
        raise Exception("Addition Error!")
    print("Testing Subtraction...")
    dp = vp - up
    if str(dp) != '[ 3.  3.  3.]':
        raise Exception("Subtraction Error!")
    print("Testing Multiplication...")
    ep = up * cint
    if str(ep) != '[ 10.  20.  30.]':
        raise Exception("Multiplication Error!")
    print("Testing Equality...")
    gp = up.copy()
    if str(gp) != '[ 1.  2.  3.]':
        raise Exception("Equality Error!")
    print("Testing Distance")
    zp = Point3D(1,2,2)
    yp = Point3D(2,4,4)
    hp = zp.distance(yp)
    if hp != 3:
        raise Exception("Distance Error!")
    print("Tests for Point3D Complete!\n---------------")
    un = Normal(1,2,3)
    vn = Normal(4,5,6)
    print("Testing Printing...")
    if str(un) != '[ 1.  2.  3.]':
        raise Exception("Printing Error!")
    print("Testing Addition...")
    cn = un + vn
    if str(cn) != '[ 5.  7.  9.]':
        raise Exception("Addition Error!")
    print("Testing Multiplication...")
    en = un * cint
    if str(en) != '[ 10.  20.  30.]':
        raise Exception("Multiplication Error!")
    print("Testing Equality...")
    nn = -un
    if str(nn) != '[-1. -2. -3.]':
        raise Exception("Negation Error!")
    print("Tests for Normal Complete!\n---------------")

    print("Testing RandomCube...")
    fll = Point3D(-1, -1, -1)
    bur = Point3D(1, 1, 1)
    points = randomCube(fll, bur, 4)
    print (points)
