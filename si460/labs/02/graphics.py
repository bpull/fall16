
# B.S. Pulllig (m175148)
import numpy as np

# The beginnings of a Vector3D - For you to edit
class Vector3D:
    def __init__(self, val, *args):
        if type(val) is np.ndarray:
            self.v = val
        elif args and len(args) == 2:
            self.v = np.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Vector3D")
    def __repr__(self):
        return str(self.v)
    def __add__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(self.v + other.v)
        if isinstance(other, Normal):
            return Vector3D(self.v + other.n)
    def __sub__(self, other):
        return Vector3D(self.v - other.v)
    def __mul__(self, c):
        return Vector3D(self.v * c)
    def __truediv__(self, c):
        return Vector3D(self.v / c)
    def copy(self):
        return Vector3D(np.copy(self.v))
    def magnitude(self):
        return np.linalg.norm(self.v)
    def square(self):
        '''returns the sum of the squares of each element'''
        return np.sum(np.square(self.v))
    def dot(self, other):
        '''returns a float. the dot product of two vectors'''
        if isinstance(other, Vector3D):
            return np.sum(np.dot(self.v, other.v))
        if isinstance(other, Normal):
            return np.sum(self.v * other.n)
    def dotangle(self, other, angle):
        '''returns dot product times an angle'''
        angle = int(angle)
        u = np.linalg.norm(self.v)
        v = np.linalg.norm(other.v)

        uv = u * v
        return uv * np.cos(angle)
    def cross(self, other):
        return Vector3D(np.cross(self.v, other.v))


class Point3D:

    def __init__(self, val, *args):
        if type(val) is np.ndarray:
            self.p = val
        elif args and len(args) == 2:
            self.p = np.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Point3D")
    def __repr__(self):
        return str(self.p)
    def __add__(self, other):
        return Point3D(self.p + other.p)
    def __sub__(self, other):
        if isinstance(other, Vector3D):
            return Vector3D(np.subtract(self.p, other.v))
        elif isinstance(other, Point3D):
            return Point3D(np.subtract(self.p, other.p))
    def distancesquared(self, other):
        subbed = self.p - other.p
        return np.sum(np.square(subbed))
    def distance(self, other):
        return np.sqrt(self.distancesquared(other))
    def copy(self):
        return Point3D(np.copy(self.p))
    def __mul__(self, c):
        return Point3D(self.p * c)


class Normal:
    
    def __init__(self, val, *args):
        if type(val) is np.ndarray:
            self.n = val
        elif args and len(args) == 2:
            self.n = np.array([val,args[0],args[1]], dtype='float64')
        else:
            raise Exception("Invalid Arguments to Normal")
    def __repr__(self):
        return str(self.n)
    def __neg__(self):
        return Normal(np.negative(self.n))
    def __add__(self, other):
        if isinstance(other, Normal):
            return Normal(self.n + other.n)
        if isinstance(other, Vector3D):
            return Vector3D(self.n + other.v)
    def __mul__(self, c):
        return Normal(self.n * c)
    def dot(self, other):
        return np.sum(self.n * other.v)

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
    cp = up + vp
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
