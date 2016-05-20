from math import sin, cos, pi, sqrt
def is_dark(pic, x, y, threshold=150):
    r = pic.getPixelRed(x,y)
    g = pic.getPixelBlue(x,y)
    b = pic.getPixelGreen(x,y)
    return r + g + b < threshold


class Char_Repr:
    def __init__(self, pic, xstart=0, ystart=0, \
            xend=None, yend=None, stepsize=60, max_lines=2):
        if not xend:
            xend=pic.width
        if not yend:
            yend=pic.height
        self.pic = pic
        self.xstart = xstart
        self.ystart = ystart
        self.xend = xend
        self.yend = yend
        self.stepsize = stepsize
        self.max_lines = max_lines
        self.points = {}
        self.gen_repr()

    def gen_repr(self):
        self.xcenter, self.ycenter = self.center_of_mass()
        for angle in range(0, 360, self.stepsize):
            points_for_angle = self.find_points(angle)
            self.points[angle] = tuple(points_for_angle)
        self.normalize()

    def normalize(self):
        pass

    def center_of_mass(self):
        xtotal = 0
        ytotal = 0
        xcount = 0
        ycount = 0
        for i in range(self.xstart, self.xend):
            for j in range(self.ystart, self.yend):
                if is_dark(self.pic, i, j):
                    xtotal += i
                    ytotal += j
                    xcount += 1
                    ycount += 1
        return xtotal // xcount, ytotal // ycount

    def in_bounds(self, x, y):
        return self.xstart <= x < self.xend and self.ystart <= y < self.yend

    def distance(self, x, y):
        return sqrt((x - self.xcenter)**2 + (y - self.ycenter)**2)

    def find_points(self, angle):
        """
        returns a list of all lines encountered in start, stop, start, stop form
        distances are from self.center_of_mass along angle
        """
        angle_rads = angle * 1.0 / 360 * 2 * pi
        points = []
        cur_pos_x = self.xcenter
        cur_pos_y = self.ycenter
        in_character = False
        while self.in_bounds(cur_pos_x, cur_pos_y):
            if in_character:
                if not is_dark(self.pic, cur_pos_x, cur_pos_y):
                    in_character = False
                    points.append(self.distance(cur_pos_x, cur_pos_y))
            else:
                if is_dark(self.pic, cur_pos_x, cur_pos_y):
                    in_character = True
                    points.append(self.distance(cur_pos_x, cur_pos_y))
            cur_pos_x += 3 * cos(angle_rads)
            cur_pos_y += 3 * sin(angle_rads)
        return points
