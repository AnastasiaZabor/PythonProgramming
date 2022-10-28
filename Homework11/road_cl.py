MASS = 25

class Road:
    _length = 0
    _width = 0

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self, thickness):
        return self._length * self._width * MASS * thickness


