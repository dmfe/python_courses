from random import seed
from random import randint
from time import time

import field as fld
import settings as st


class ApplesController:

    def __init__(self, canvas, settings):
        seed(round(time()))

        self._canvas = canvas
        self._settings = settings
        self._apples = []
        self._field = fld.Field(st.FRAME_SPAN, st.FRAME_SPAN,
                                self._settings.width + st.FRAME_SPAN,
                                self._settings.height + st.FRAME_SPAN,
                                '#585858')

    def set_apples_count(self, count):
        self._settings.apples_count = count

    def draw_field(self):
        self._canvas.create_rectangle(self._field.x_left,
                                      self._field.y_top,
                                      self._field.x_right,
                                      self._field.y_bottom,
                                      fill=self._field.background)

    def draw_apples(self):
        self._generate_apples()
        for apple in self._apples:
            self._canvas.create_oval(apple.get_x_center() - apple.get_radius(),
                                     apple.get_y_center() - apple.get_radius(),
                                     apple.get_x_center() + apple.get_radius(),
                                     apple.get_y_center() + apple.get_radius(),
                                     fill='#E1F18E')

        print(f'Generated applese count: {len(self._apples)}')

    def check_if_collided(self):
        is_collided = False

        apple_ids_map = {id(apple) : apple for apple in self._apples}
        for apple in self._apples:
            del apple_ids_map[id(apple)]
            for other in apple_ids_map.values():
                if apple.is_collided(other):
                    is_collided = True
                if is_collided:
                    break
            if is_collided:
                break

        return is_collided

    def _generate_apples(self):
        self._apples.clear()
        limit_count = 0
        while len(self._apples) < self._settings.apples_count:
            radius = randint(self._settings.radius_min, self._settings.radius_max)
            x_center = randint(self._field.x_left + radius, self._field.x_right - radius)
            y_center = randint(self._field.y_top + radius, self._field.y_bottom - radius)
            apple = fld.Apple(x_center, y_center, radius)

            is_collided = False
            for other in self._apples:
                if apple.is_collided(other):
                    is_collided = True
                    limit_count += 1
                    break

            if not is_collided:
                limit_count = 0
                self._apples.append(apple)

            if limit_count == self._settings.fail_limit:
                break
