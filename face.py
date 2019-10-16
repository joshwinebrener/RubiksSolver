# A Face is a point outside the cube with a certain position and color, which can
# be thought to be projected onto the Cube.  The origin is the center of the Cube.
class Face:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        return