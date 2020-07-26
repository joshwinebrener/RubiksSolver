import math

# A Face is a point outside the cube with a certain position and color, which can
# be thought to be projected onto the Cube.  The origin is the center of the Cube.
class Face:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        return
    
    def isEdgePiece(self):
        return (self.x == 0 and self.y != 0 and self.z != 0) \
            or (self.x != 0 and self.y == 0 and self.z != 0) \
            or (self.x != 0 and self.y != 0 and self.z == 0)
    
    def isCornerPiece(self):
        # return (abs(self.x) == 2 and abs(self.y) > 2 and abs(self.z) > 2) \
        #     or (abs(self.x) > 2 and abs(self.y) == 2 and abs(self.z) > 2) \
        #     or (abs(self.x) > 2 and abs(self.y) > 2 and abs(self.z) == 2)
        return self.x ** 2 + self.y ** 2 + self.z ** 2 == 6
    
    # Returns a list of x, y, z coordinates of the face that should be connected to
    # self.  Returns 6 integers if it is a corner piece.
    def adjacentCoordinates(self):
        mag_x = abs(self.x)
        mag_y = abs(self.y)
        mag_z = abs(self.z)

        sign_x = self.x / mag_x if mag_x != 0 else 1
        sign_y = self.y / mag_y if mag_y != 0 else 1
        sign_z = self.z / mag_z if mag_z != 0 else 1

        if self.isEdgePiece():
            adjacentX = (0 if mag_x == 0 else 1 if mag_x == 2 else 2) * sign_x
            adjacentY = (0 if mag_y == 0 else 1 if mag_y == 2 else 2) * sign_y
            adjacentZ = (0 if mag_z == 0 else 1 if mag_z == 2 else 2) * sign_z
            return [adjacentX, adjacentY, adjacentZ]
        else:
            # TODO: ensure that left coordinates are actually to the left of the face
            #   It may be necessary to work on the adjacent face check in corners.py
            leftX = (1 if mag_x == 2 else 2)
            leftY = (1 if mag_y == 2 or leftX == 2 else 2)
            leftZ = (1 if mag_z == 2 or leftX == 2 or leftY == 2 else 2)
            rightX = (1 if mag_x == 2 or leftX == 2 else 2)
            rightY = (1 if mag_y == 2 or leftY == 2 else 2)
            rightZ = (1 if mag_z == 2 or leftZ == 2 else 2)
            leftX *= sign_x
            leftY *= sign_y
            leftZ *= sign_z
            rightX *= sign_x
            rightY *= sign_y
            rightZ *= sign_z
            return [leftX, leftY, leftZ, rightX, rightY, rightZ]
    
    def currentSide(self):
        if self.x == 2:
            return 'r'
        elif self.y == 2:
            return 'b'
        elif self.z == 2:
            return 'w'
        elif self.x == -2:
            return 'o'
        elif self.y == -2:
            return 'g'
        elif self.z == -2:
            return 'y'

    def onCorrectSide(self):
        return self.color == self.currentSide()
    
    def adjacentSide(self):
        if self.isEdgePiece():
            if self.x == 1:
                return 'r'
            elif self.y == 1:
                return 'b'
            elif self.z == 1:
                return 'w'
            elif self.x == -1:
                return 'o'
            elif self.y == -1:
                return 'g'
            elif self.z == -1:
                return 'y'
    
    def rightAdjacent(self):
        if self.isCornerPiece():
            if self.x == 1 and (self.y**2 < self.z**2 if self.z * self.y > 0 else self.y**2 > self.z**2):
                return 'r'
            elif self.y == 1 and (self.z**2 < self.x**2 if self.x * self.z > 0 else self.z**2 > self.x**2):
                return 'b'
            elif self.z == 1 and (self.x**2 < self.y**2 if self.y * self.x > 0 else self.x**2 > self.y**2):
                return 'w'
            elif self.x == -1 and (self.z**2 < self.y**2 if self.y * self.z > 0 else self.z**2 > self.y**2):
                return 'o'
            elif self.y == -1 and (self.x**2 < self.z**2 if self.z * self.x > 0 else self.x**2 > self.z**2):
                return 'g'
            elif self.z == -1 and (self.y**2 < self.x**2 if self.x * self.y > 0 else self.y**2 > self.x**2):
                return 'y'

    def leftAdjacent(self):
        if self.isCornerPiece():
            if self.x == 1 and (self.y**2 > self.z**2 if self.z * self.y > 0 else self.y**2 < self.z**2):
                return 'r'
            elif self.y == 1 and (self.z**2 > self.x**2 if self.x * self.z > 0 else self.z**2 < self.x**2):
                return 'b'
            elif self.z == 1 and (self.x**2 > self.y**2 if self.y * self.x > 0 else self.x**2 < self.y**2):
                return 'w'
            elif self.x == -1 and (self.z**2 > self.y**2 if self.y * self.z > 0 else self.z**2 < self.y**2):
                return 'o'
            elif self.y == -1 and (self.x**2 > self.z**2 if self.z * self.x > 0 else self.x**2 < self.z**2):
                return 'g'
            elif self.z == -1 and (self.y**2 > self.x**2 if self.x * self.y > 0 else self.y**2 < self.x**2):
                return 'y'