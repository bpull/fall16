from graphics import *

class PPM:

    def __init__(self, vp, filename):
        with open(filename, 'w') as f:
            f.write('P3\n')
            f.write(str(vp.hres)+" "+str(vp.vres)+"\n")
            f.write("255\n")
            for i in range(vp.vres-1, -1, -1):
                for j in range(vp.hres):
                    color = vp.get_color(i,j)
                    r,g,b = color.get()
                    r = int(r * 255)
                    g = int(g * 255)
                    b = int(b * 255)
                    f.write(str(r)+" "+str(g)+" "+str(b)+" ")
                f.write("\n")
