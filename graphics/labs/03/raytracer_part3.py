from graphics import *

class raytracer:

    def __init__(self, vp, objects):
        self.vp = vp
        self.objects = objects

    def color_plane(self):
        hres,vres = vp.get_resolution()

        for row in vres:
            for col in hres:
                self.color_pixel(row,col)

    def color_pixel(self, row, col):
        min_t = 1000
        min_color = ColorRGB(1,1,1)
        for obj in self.objects:
            tryhit, t, p, color = obj.hit(vp.orthographic_ray(row,col), 10e-6)
            if tryhit:
                if t < min_t:
                    min_t = t
                    min_color = color
        self.vp.set_color(row, col, min_color)

    def get_viewplane(self):
        return self.vp
