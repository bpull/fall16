from graphics import *

class raytracer:

    def __init__(self, vp, objects):
        self.vp = vp
        self.objects = objects

    def color_plane(self):
        hres,vres = self.vp.get_resolution()

        for row in range(vres):
            for col in range(hres):
                self.color_pixel(row,col)

    def color_plane_challenge(self, ray):
        hres,vres = self.vp.get_resolution()

        for row in range(vres):
            for col in range(hres):
                self.color_pixel_challenge(row,col,ray)

    def color_pixel(self, row, col):
        min_t = 100000
        min_color = ColorRGB(1,1,1)
        for obj in self.objects:
            tryhit, t, p, color = obj.hit(self.vp.orthographic_ray(row,col), 10e-6)
            if tryhit:
                if t < min_t:
                    min_t = t
                    min_color = color
        self.vp.set_color(row,col, min_color)

    def color_pixel_challenge(self, row, col, ray):
        min_t = 100000
        min_color = ColorRGB(1,1,1)
        for obj in self.objects:
            tryhit, t, p, color = obj.hit(self.vp.perspective_ray(row,col,ray), 10e-6)
            if tryhit:
                if t < min_t:
                    min_t = t
                    min_color = color
        self.vp.set_color(row,col, min_color)

    def get_viewplane(self):
        return self.vp

if __name__ == '__main__':
    S1 = Sphere(Point3D(300,200,200), 100, ColorRGB(1.0,0.2,0.4))
    S2 = Sphere(Point3D(-200,-100,50), 35, ColorRGB(0.3,0.8,0.2))
    S3 = Sphere(Point3D(50,20,100), 25, ColorRGB(0.4,0.1,0.4))
    S4 = Sphere(Point3D(300,-200,600), 250, ColorRGB(0.6,0.6,0.4))
    S5 = Sphere(Point3D(400,400,900), 400, ColorRGB(0.0,0.2,1.0))

    # Build the Planes that will be in our world
    P1 = Plane(Point3D(50,50,999), Normal(0,0,1), ColorRGB(0.8,0.8,0.8))
    P2 = Plane(Point3D(50,50,900), Normal(1,1,1), ColorRGB(1.0,1.0,1.0))

    vp = ViewPlane(Point3D(0,0,0), Normal(0,0,1), 640, 480, 1.0)
    objects = []
    objects.append(S1)
    objects.append(S2)
    objects.append(S3)
    objects.append(S4)
    objects.append(S5)
    objects.append(P1)
    objects.append(P2)

    rt = raytracer(vp, objects)
    rt.color_plane()
