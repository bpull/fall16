import math

def dimensions(s1, s2, a2):
    '''Given two parallel lines of two triangles and the internal angle of triangle 2, all dimensions will be returned'''
    tri2angle1 = float(a2)
    tri2angle2 = 90 - tri2angle1

    tri2opp = float(s2)
    tri2hyp = tri2opp / math.sin(tri2angle1 * math.pi/180)
    tri2adj = tri2opp / math.cos(tri2angle1 * math.pi/180)

    tri1opp = float(s1)
    tri1adj = tri2adj
    tri1hyp = math.sqrt(math.pow(tri1opp, 2) + math.pow(tri1adj, 2))

    tri1angle1 = math.atan(tri1opp/tri1adj)
    tri1angle1 = tri1angle1 * 180 / math.pi
    tri1angle2 = 90 - tri1angle1

    print ("Triangle 1 angles: "+str(tri1angle1)+" deg and "+str(tri1angle2)+" deg")
    print ("Triangle 1 sides: "+str(tri1opp)+", "+str(tri1adj)+", and "+str(tri1hyp)+"\n")
    print ("Triangle 2 angles: "+str(tri2angle1)+" deg and "+str(tri2angle2)+" deg")
    print ("Triangle 2 sides: "+str(tri2opp)+", "+str(tri2adj)+", and "+str(tri2hyp)+"\n")

dimensions(9, 6, 31)
