class Char_Repr:
    def __init__(self, pic, xstart=0, ystart=0, \
            xend=None, yend=None, stepsize=60):
        if not xend:
            xend=pic.width
        if not yend:
            yend=pic.height
        self.stepsize = stepsize
        self.points = {}
        self.gen_repr(pic, xstart, ystart, xend, yend)

    def gen_repr(self, pic, xstart, ystart, xend, yend):
        xcenter, ycenter = self.center_of_mass(pic, xstart, ystart, xend, yend)
        for angle in range(0, 360, self.stepsize):
            points_for_angle = find_points(pic, xcenter, ycenter, angle)
            self.points[angle] = tuple(normalized_points)
        self.normalize()

    def normalize(self):
        pass

    def find_points(pic, xcenter, ycenter, angle):
        pass
