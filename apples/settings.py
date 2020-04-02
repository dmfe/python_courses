
WIDTH = 500
HEIGHT = 300
DEFAULT_APPLES_COUNT = 50
DEFAULT_MIN_RADIUS = 10
DEFAULT_MAX_RADIUS = 50
FRAME_SPAN = 10
DEFAULT_FAIL_LIMIT = 10000


class ApplesGeneratorSetting:
    def __init__(self, width, height, count, radius_min, radius_max, fail_limit):
        self.width = width
        self.height = height
        self.apples_count = count
        self.radius_min = radius_min
        self.radius_max = radius_max
        self.fail_limit = fail_limit


class ApplesGeneratorSettingBuilder:
    def __init__(self):
        self.width = WIDTH
        self.height = HEIGHT
        self.apples_count = DEFAULT_APPLES_COUNT
        self.radius_min = DEFAULT_MIN_RADIUS
        self.radius_max = DEFAULT_MAX_RADIUS
        self.fail_limit = DEFAULT_FAIL_LIMIT

    def width(self, width):
        self.width = width
        return self

    def height(self, height):
        self.height = height
        return self

    def apples_count(self, apples_count):
        self.apples_count = apples_count
        return self

    def radius_min(self, radius_min):
        self.radius_min = radius_min
        return self

    def radius_max(self, radius_max):
        self.radius_max = radius_max
        return self

    def build(self):
        return ApplesGeneratorSetting(self.width, self.height, self.apples_count,
                                      self.radius_min, self.radius_max, self.fail_limit)
