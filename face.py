# A Face is a point outside the cube with a certain position and color, which can
# be thought to be projected onto the Cube.  The origin is the center of the Cube.
# Rather than using x, y, and z values, it is easier to use wy (white to yellow),
# ro (red to orange), and bg (blue to green)
class Face:
    def __init__(self, wy, ro, bg, color):
        self.wy = wy
        self.ro = ro
        self.bg = bg
        self.color = color
        return