import math
from face import Face
from random import randrange

class Cube:
    def __init__(self):
        self.faces = []
        # populate white and yellow faces
        for x in range(-1, 2):
            for y in range(-1, 2):
                self.faces.append(Face(x, y, 2, 'w'))
                self.faces.append(Face(x, y, -2, 'y'))
        # populate red and orange faces
        for y in range(-1, 2):
            for z in range(-1, 2):
                self.faces.append(Face(2, y, z, 'r'))
                self.faces.append(Face(-2, y, z, 'o'))
        # populate blue and green faces
        for x in range(-1, 2):
            for z in range(-1, 2):
                self.faces.append(Face(x, 2, z, 'b'))
                self.faces.append(Face(x, -2, z, 'g'))
        return

    # Side can be int for random generation.
    # Num is the number of clockwise quarter turns.  Set num to 3 for a back turn
    def turn(self, side, num):
        # Convert number of clockwise quarter turns to counterclockwise radians
        _theta = num % 4 * - math.pi / 2
        sinTheta = int(round(math.sin(_theta)))
        cosTheta = int(round(math.cos(_theta)))

        # Transform the coordinates of the faces depending on which side they are on
        for face in self.faces:
            # Side 1 is white
            if (side == 1 or side == 'w') and face.z > 0:
                # [cos -sin 0] [x]
                # [sin cos  0]*[y]
                # [0   0    1] [z]
                _x = face.x * cosTheta - face.y * sinTheta
                _y = face.x * sinTheta + face.y * cosTheta
                face.x = _x
                face.y = _y
            # Side 2 is red
            elif (side == 2 or side == 'r') and face.x > 0:
                # [1 0   0   ] [x]
                # [0 cos -sin]*[y]
                # [0 sin cos ] [z]
                _y = face.y * cosTheta - face.z * sinTheta
                _z = face.y * sinTheta + face.z * cosTheta
                face.y = _y
                face.z = _z
            # Side 3 is blue
            elif (side == 3 or side == 'b') and face.y > 0:
                # [cos  0 sin] [x]
                # [0    1 0  ]*[y]
                # [-sin 0 cos] [z]
                _x = face.x * cosTheta + face.z * sinTheta
                _z = -face.x * sinTheta + face.z * cosTheta
                face.x = _x
                face.z = _z
            # Side 4 is orange
            elif (side == 4 or side == 'o') and face.x < 0:
                # [1 0   0   ] [x]
                # [0 cos sin ]*[y]
                # [0 -sin cos] [z]
                _y = face.y * cosTheta + face.z * sinTheta
                _z = -face.y * sinTheta + face.z * cosTheta
                face.y = _y
                face.z = _z
            # Side 5 is green
            elif (side == 5 or side == 'g') and face.y < 0:
                # [cos 0 -sin] [x]
                # [0   1 0   ]*[y]
                # [sin 0 cos ] [z]
                _x = face.x * cosTheta - face.z * sinTheta
                _z = face.x * sinTheta + face.z * cosTheta
                face.x = _x
                face.z = _z
            # Side 6 is yellow
            elif (side == 6 or side == 'y') and face.z < 0:
                # [cos  sin 0] [x]
                # [-sin cos 0]*[y]
                # [0    0   1] [z]
                _x = face.x * cosTheta + face.y * sinTheta
                _y = -face.x * sinTheta + face.y * cosTheta
                face.x = _x
                face.y = _y
        return

    def input(self):
        print('Type in the color of the stickers around each center piece:')
        print('w for white, r for red, b for blue, o for orange, g for green, and y for yellow')
        print('type q to quit, u to undo')

        # Top face:
        print('-  -  -  1  2  3  -  -  -  -  -  -')
        print('-  -  -  4  w  5  -  -  -  -  -  -')
        print('-  -  -  6  7  8  -  -  -  -  -  -')
        print('9  10 11 17 18 19 25 26 27 33 34 35')
        print('12 g  13 20 r  21 28 b  29 36 o  37')
        print('14 15 16 22 23 24 30 31 32 38 39 40')
        print('-  -  -  41 42 43  -  -  -  -  -  -')
        print('-  -  -  44 y  45  -  -  -  -  -  -')
        print('-  -  -  46 47 48  -  -  -  -  -  -')

        colors = []

        # Collect colors from user
        i = 0
        while i < 48:
            color = input('face {0}: '.format(i + 1))
            if color == 'w' or color == 'r' or color == 'b' or color == 'o' or color == 'g' or color == 'y':
                colors.insert(i, color)
            elif color == 'q':
                print('quitting cube input...\n')
                break
            elif color == 'u' and i > 1:
                print('undoing last entry...')
                i -= 2
            else:
                print('not a valid color.  Make sure that the input character was w, r, b, o, g, or y.\nTrying again...')
                i -= 1
            i += 1
            if i/8 == 1: print("\n\nWhite side input complete!\n")
            elif i/8 == 2: print("\n\nGreen side input complete!\n")
            elif i/8 == 3: print("\n\nRed side input complete!\n")
            elif i/8 == 4: print("\n\nBlue side input complete!\n")
            elif i/8 == 5: print("\n\nOrange side input complete!\n")
            elif i/8 == 6: print("\n\nYellow side input complete!\n")
        
        print("**************************************************************************************************\n")
        
        self.faces = []

        # Arrange colors as faces
        for i in range(48):
            index = i # Stores which of the 9 faces (including the center) our current face is
            index %= 8
            # Compensate for the missing center piece
            if index > 3:
                index += 1

            face = math.floor(i / 8)
            if face == 0: # White face
                z = 2
                x = index % 3 - 1 # Mod left to right
                y = math.floor(index / 3) - 1 # Division top to bottom
            elif face == 1: # Green face
                y = -2
                x = index % 3 - 1
                z = 1 - math.floor(index / 3)
            elif face == 2: # Red face
                x = 2
                y = index % 3 - 1
                z = 1 - math.floor(index / 3)
            elif face == 3: # Blue face
                y = 2
                x = 1 - (index % 3)
                z = 1 - math.floor(index / 3)
            elif face == 4: # Orange face
                x = -2
                y = 1 - (index % 3)
                z = 1 - math.floor(index / 3)
            elif face == 5: # Yellow face
                z = -2
                x = index % 3 - 1
                y = 1 - math.floor(index / 3)
                
            self.faces.append(Face(x, y, z, colors[i]))
        
        # Add the static center faces
        self.faces.append(Face(0, 0, 2, 'w'))
        self.faces.append(Face(0, -2, 0, 'g'))
        self.faces.append(Face(2, 0, 0, 'r'))
        self.faces.append(Face(0, 2, 0, 'b'))
        self.faces.append(Face(-2, 0, 0, 'o'))
        self.faces.append(Face(0, 0, -2, 'y'))


    
    def printFaces(self):
        # Initialize a 9x12 2d list of characters.  These will represent the colors of 
        # the faces, with spaces where there is no face.
        _colors = []
        for y in range(9):
            _colors.append([])
            for x in range(12):
                _colors[y].append("-")

        for face in self.faces:
            # insert top faces
            if face.z == 2:
                _colors[face.x + 1][face.y + 4] = face.color
            # insert bottom faces
            elif face.z == -2:
                _colors[-face.x + 7][face.y + 4] = face.color
            # insert front faces
            elif face.x == 2:
                _colors[-face.z + 4][face.y + 4] = face.color
            # insert back faces
            elif face.x == -2:
                _colors[-face.z + 4][-face.y + 10] = face.color
            # insert right faces
            elif face.y == 2:
                _colors[-face.z + 4][-face.x + 7] = face.color
            # insert left faces
            elif face.y == -2:
                _colors[-face.z + 4][face.x + 1] = face.color
        
        print('*-----------------------*')
        for y in range(9):
            print('|' + ' '.join(_colors[y]) + '|')
        print('*-----------------------*\n')
        return
    
    def sisterFaces(self, face):
        adj = face.adjacentCoordinates()
        if len(adj) == 6:
            return [self.at(adj[0], adj[1], adj[2]), self.at(adj[3], adj[4], adj[5])]
        else:
            return self.at(adj[0], adj[1], adj[2])

    def at(self, x, y, z):
        for face in self.faces:
            if face.x == x and face.y == y and face.z == z:
                return face
        print("Face not found with coordinates ", str(x), str(y), str(z))
        return
    
    # def onCorrectSide(self, face):
    #     if face.x == 2:
    #         return face.color == 'r'
    #     elif face.y == 2:
    #         return face.color == 'b'
    #     elif face.z == 2:
    #         return face.color == 'w'
    #     elif face.x == -2:
    #         return face.color == 'o'
    #     elif face.y == -2:
    #         return face.color == 'g'
    #     elif face.z == -2:
    #         return face.color == 'y'
        
    
    def scramble(self):
        for i in range(20):
            self.turn(randrange(1, 7), randrange(1, 4))