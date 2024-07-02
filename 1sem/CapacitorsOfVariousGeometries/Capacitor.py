class Capacitor:
    def __init__(self, length, width, d, e, radius):
        self.length = length / 100
        self.width = width / 100
        self.dist = d / 1000
        self.e = e
        self.radius = radius / 100
        self.is_circle = False

    def get_area(self):
        if self.is_circle:
            return self.radius**2*3.14
        return self.width * self.length

    def set_data(self, length, width, dist, e, radius):
        self.length = length / 100
        self.width = width / 100
        self.e = e
        self.radius = radius / 100
        self.dist = dist / 1000

    def pool_capacitor(self):
        e_0 = 8.854 * 10 ** (-12)
        c_base = self.e * e_0 * self.get_area() / self.dist
        return c_base
