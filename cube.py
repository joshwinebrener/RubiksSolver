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
        for x in range(-1, 2):
            for z in range(-1, 2):
                self.faces.append(Face(x, 2, z, 'r'))
                self.faces.append(Face(x, -2, z, 'o'))
        # populate blue and green faces
        for y in range(-1, 2):
            for z in range(-1, 2):
                self.faces.append(Face(2, y, z, 'b'))
                self.faces.append(Face(-2, y, z, 'g'))
        return

    # Side is int for random generation.
    # Num is the number of clockwise quarter turns.  Set num to 3 for a back turn
    def turn(self, side, num):
        # Convert number of clockwise quarter turns to counterclockwise radians
        _theta = num % 4 * - math.pi / 2

        # Transform the coordinates of the faces depending on which side they are on
        for face in self.faces:
            # Side 1 is white
            if (side == 1 or side == 'w') and face.z > 0:
                _x = face.x * int(round(math.cos(-_theta))) - face.y * int(round(math.sin(-_theta)))
                _y = face.x * int(round(math.sin(-_theta))) + face.y * int(round(math.cos(-_theta)))              
                face.x = _x
                face.y = _y
            # Side 2 is red
            elif (side == 2 or side == 'r') and face.y > 0:
                _x = face.x * int(round(math.cos(_theta))) - face.z * int(round(math.sin(_theta)))
                _z = face.x * int(round(math.sin(_theta))) + face.z * int(round(math.cos(_theta)))
                face.x = _x
                face.z = _z
            # Side 3 is blue
            elif (side == 3 or side == 'b') and face.x > 0:
                _y = face.y * int(round(math.cos(-_theta))) - face.z * int(round(math.sin(-_theta)))
                _z = face.y * int(round(math.sin(-_theta))) + face.z * int(round(math.cos(-_theta)))
                face.y = _y
                face.z = _z
            # Side 4 is orange
            elif (side == 4 or side == 'o') and face.y < 0:
                _x = face.x * int(round(math.cos(-_theta))) - face.z * int(round(math.sin(-_theta)))
                _z = face.x * int(round(math.sin(-_theta))) + face.z * int(round(math.cos(-_theta)))
                face.x = _x
                face.z = _z
            # Side 5 is green
            elif (side == 5 or side == 'g') and face.x < 0:
                _y = face.y * int(round(math.cos(_theta))) - face.z * int(round(math.sin(_theta)))
                _z = face.y * int(round(math.sin(_theta))) + face.z * int(round(math.cos(_theta)))
                face.y = _y
                face.z = _z
            # Side 6 is yellow
            elif (side == 6 or side == 'y') and face.z < 0:
                _x = face.x * int(round(math.cos(_theta))) - face.y * int(round(math.sin(_theta)))
                _y = face.x * int(round(math.sin(_theta))) + face.y * int(round(math.cos(_theta)))
                face.x = _x
                face.y = _y
        return

    # A match is defined as an edge lined up with either a corner or 2 centers
    def numOfMatches(self):
        _edgeFaces = []
        _cornerFaces = []
        _centerFaces = []
        numOfMatches = 0
        # Sort face array into three new arrays, _edgeFaces, _cornerFaces, and _centerFaces
        for face in self.faces:
            if sorted([abs(face.x), abs(face.y), abs(face.z)]) == [0, 1, 2]:
                _edgeFaces.append(face)
            if sorted([abs(face.x), abs(face.y), abs(face.z)]) == [1, 1, 2]:
                _cornerFaces.append(face)
            else:
                _centerFaces.append(face)
        for ef in _edgeFaces:
            for cf in _cornerFaces:
                if (ef.x == cf.x and ef.y == cf.y) or (ef.y == cf.y and ef.z == cf.z) or (ef.x == cf.x and ef.z == cf.z):
                    numOfMatches += 1
            # for cf in _centerFaces:
            #     if (ef.x == cf.x and ef.y == cf.y) or (ef.y == cf.y and ef.z == cf.z) or (ef.x == cf.x and ef.z == cf.z):
            #         numOfMatches += 1
        return numOfMatches

    def input(self):
        print('Type in the color of the stickers around each center piece:')
        print('w for white, r for red, b for blue, o for orange, g for green, and y for yellow')
        print('type q to quit')
        # j = 0
        # for i in range(9):
        #     if i <3 or i >= 6:
        #         print('-  -  -  {0:2d} {1:2d} {2:2d}  -  -  -  -  -  -'.format(j, j+1, j+2))
        #         j += 3
        #     elif i < 6:
        #         print('{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d} {7:2d} {8:2d} {9:2d} {10:2d} {11:2d}'.format(j, j+1, j+2, j+3, j+4, j+5, j+6, j+7, j+8, j+9, j+10, j+11))
        #         j += 9
        # faces = []
        # i = 0
        # while i < 44:
            # face = input('face {0}: '.format(i))
            # if face == 'w' or face == 'r' or face == 'b' or face == 'o' or face == 'g' or face == 'y':
            #     faces.insert(i, face)
            # elif face == 'q':
            #     print('quitting cube input...\n')
            #     faces = []
            #     break
            # else:
            #     print('not a valid color.  Make sure that the input character was w, r, b, o, g, or y.\nTrying again...')
            #     i -= 1
            # i += 1

        # Top face:
        print('-  -  -  1  2  3  -  -  -  -  -  -')
        print('-  -  -  4  w  5  -  -  -  -  -  -')
        print('-  -  -  6  7  8  -  -  -  -  -  -')
        print('9  10 11 17 18 19 25 26 27 33 34 35')
        print('12 g  13 20 r  21 28 b  29 36 o  37')
        print('14 15 16 22 23 24 30 31 32 38 39 40')
        print('-  -  - 41 42 43  -  -  -  -  -  -')
        print('-  -  - 44 y  45  -  -  -  -  -  -')
        print('-  -  - 46 47 48  -  -  -  -  -  -')

        colors = []

        # Collect colors from user
        for i in range(48):
            color = input('face {0}: '.format(i + 1))
            if color == 'w' or color == 'r' or color == 'b' or color == 'o' or color == 'g' or color == 'y':
                colors.insert(i, color)
            elif color == 'q':
                print('quitting cube input...\n')
                faces = []
                break
            else:
                print('not a valid color.  Make sure that the input character was w, r, b, o, g, or y.\nTrying again...')
                i -= 1
            i += 1
        
        # Arrange colors as faces
        for i in range(48):
            face = math.floor(i / 8)
            # TODO: add 2nd and 3rd dimension with mod function
            if face == 0: # White face
                z = 2
            elif face == 1: # Green face
                y = -2
            elif face == 2: # Red face
                x = 2
            elif face == 3: # Blue face
                y = 2
            elif face == 4: # Orange face
                x = -2
            elif face == 5: # Yellow face
                z = -2


    
    def printFaces(self):
        # Initialize a 9x12 2d list of characters.  These will represent the colors of 
        # the faces, with spaces where there is no face.
        _colors = []
        for y in range(9):
            _colors.insert(y, [])
            for x in range(12):
                _colors[y].insert(x, ' ')

        for face in self.faces:
            # insert top faces
            if face.z == 2:
                _colors[face.y + 1][face.x + 4] = face.color
            # insert bottom faces
            elif face.z == -2:
                _colors[-face.y + 7][face.x + 4] = face.color
            # insert front faces
            elif face.y == 2:
                _colors[-face.z + 4][face.x + 4] = face.color
            # insert back faces
            elif face.y == -2:
                _colors[-face.z + 4][-face.x + 10] = face.color
            # insert right faces
            elif face.x == 2:
                _colors[-face.z + 4][-face.y + 7] = face.color
            # insert left faces
            elif face.x == -2:
                _colors[-face.z + 4][face.y + 1] = face.color
        
        print('-------------------------')
        for y in range(9):
            print('|' + ' '.join(_colors[y]) + '|')
        print('-------------------------')
        return
    
    def scramble(self):
        for i in range(20):
            self.turn(randrange(1, 7), randrange(1, 4))