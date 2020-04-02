import math


class Field:

    def __init__(self, x_left, y_top, x_right, y_bottom, background):
        self.x_left = x_left
        self.y_top = y_top
        self.x_right = x_right
        self.y_bottom = y_bottom
        self.background = background

class Apple:

    def __init__(self, x_center, y_center, radius):
        self._x_center = x_center
        self._y_center = y_center
        self._radius = radius

    def get_x_center(self):
        return self._x_center

    def set_x_center(self, val):
        self._x_center = val

    def get_y_center(self):
        return self._y_center

    def set_y_center(self, val):
        self._y_center = val

    def get_radius(self):
        return self._radius

    def set_redius(self, val):
        self._radius = val

    def get_info(self):
        return (f'x center: {self._x_center}',
                f'y center: {self._y_center}',
                f'radius: {self._radius}')

    def is_collided(self, other):
        distance = math.sqrt(abs(other.get_x_center() - self._x_center)**2 + \
                             abs(other.get_y_center() - self._y_center)**2)

        return distance < other.get_radius() + self._radius
