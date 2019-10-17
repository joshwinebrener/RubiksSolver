import math
from face import Face
from random import randrange

class Cube:
    def __init__(self):
        self.faces = []
        # populate wyite and yellow faces
        for bg in range(-1, 2):
            for ro in range(-1, 2):
                self.faces.append(Face(2, ro, bg, 'w'))
                self.faces.append(Face(-2, ro, bg, 'y'))
        # populate red and orange faces
        for bg in range(-1, 2):
            for wy in range(-1, 2):
                self.faces.append(Face(wy, 2, bg, 'r'))
                self.faces.append(Face(wy, -2, bg, 'o'))
        # populate blue and green faces
        for ro in range(-1, 2):
            for wy in range(-1, 2):
                self.faces.append(Face(wy, ro, 2, 'b'))
                self.faces.append(Face(wy, ro, -2, 'g'))
        return

    # Side is int for random generation.
    # Num is the number of clockwise quarter turns.  Set num to 3 for a back turn
    def turn(self, side, num):
        # Convert number of clockwise quarter turns to counterclockwise radians
        _theta = num % 4 * - math.pi / 2

        # Transform the coordinates of the faces depending on wyich side they are on
        for face in self.faces:
            # Side 1 is wyite
            if (side == 1 or side == 'w') and face.wy > 0:
                bg = face.bg * int(round(math.cos(-_theta))) - face.ro * int(round(math.sin(-_theta)))
                ro = face.bg * int(round(math.sin(-_theta))) + face.ro * int(round(math.cos(-_theta)))              
                face.bg = bg
                face.ro = ro
            # Side 2 is red
            elif (side == 2 or side == 'r') and face.ro > 0:
                bg = face.bg * int(round(math.cos(_theta))) - face.wy * int(round(math.sin(_theta)))
                wy = face.bg * int(round(math.sin(_theta))) + face.wy * int(round(math.cos(_theta)))
                face.bg = bg
                face.wy = wy
            # Side 3 is blue
            elif (side == 3 or side == 'b') and face.bg > 0:
                ro = face.ro * int(round(math.cos(-_theta))) - face.wy * int(round(math.sin(-_theta)))
                wy = face.ro * int(round(math.sin(-_theta))) + face.wy * int(round(math.cos(-_theta)))
                face.ro = ro
                face.wy = wy
            # Side 4 is orange
            elif (side == 4 or side == 'o') and face.ro < 0:
                bg = face.bg * int(round(math.cos(-_theta))) - face.wy * int(round(math.sin(-_theta)))
                wy = face.bg * int(round(math.sin(-_theta))) + face.wy * int(round(math.cos(-_theta)))
                face.bg = bg
                face.wy = wy
            # Side 5 is green
            elif (side == 5 or side == 'g') and face.bg < 0:
                ro = face.ro * int(round(math.cos(_theta))) - face.wy * int(round(math.sin(_theta)))
                wy = face.ro * int(round(math.sin(_theta))) + face.wy * int(round(math.cos(_theta)))
                face.ro = ro
                face.wy = wy
            # Side 6 is yellow
            elif (side == 6 or side == 'y') and face.wy < 0:
                bg = face.bg * int(round(math.cos(_theta))) - face.ro * int(round(math.sin(_theta)))
                ro = face.bg * int(round(math.sin(_theta))) + face.ro * int(round(math.cos(_theta)))
                face.bg = bg
                face.ro = ro
        return

    # A match is defined as an edge lined up with either a corner or 2 centers
    def numOfMatches(self):
        _edgeFaces = []
        _cornerFaces = []
        _centerFaces = []
        numOfMatches = 0
        # Sort face array into three new arrays, _edgeFaces, _cornerFaces, and _centerFaces
        for face in self.faces:
            if sorted([abs(face.bg), abs(face.ro), abs(face.wy)]) == [0, 1, 2]:
                _edgeFaces.append(face)
            if sorted([abs(face.bg), abs(face.ro), abs(face.wy)]) == [1, 1, 2]:
                _cornerFaces.append(face)
            else:
                _centerFaces.append(face)
        for ef in _edgeFaces:
            for cf in _cornerFaces:
                if (ef.bg == cf.bg and ef.ro == cf.ro) or (ef.ro == cf.ro and ef.wy == cf.wy) or (ef.bg == cf.bg and ef.wy == cf.wy):
                    numOfMatches += 1
            # for cf in _centerFaces:
            #     if (ef.bg == cf.bg and ef.ro == cf.ro) or (ef.ro == cf.ro and ef.wy == cf.wy) or (ef.bg == cf.bg and ef.wy == cf.wy):
            #         numOfMatches += 1
        return numOfMatches

    def input(self):
        print('Type in the color of the stickers around each center piece:')
        print('w for wyite, r for red, b for blue, o for orange, g for green, and y for yellow')
        print('type q to quit')
        j = 0
        for i in range(9):
            if i <3 or i >= 6:
                print('-  -  -  {0:2d} {1:2d} {2:2d}  -  -  -  -  -  -'.format(j, j+1, j+2))
                j += 3
            elif i < 6:
                print('{0:2d} {1:2d} {2:2d} {3:2d} {4:2d} {5:2d} {6:2d} {7:2d} {8:2d} {9:2d} {10:2d} {11:2d}'.format(j, j+1, j+2, j+3, j+4, j+5, j+6, j+7, j+8, j+9, j+10, j+11))
                j += 9
        faces = []
        i = 0
        while i < 44:
            face = input('face {0}: '.format(i))
            if face == 'w' or face == 'r' or face == 'b' or face == 'o' or face == 'g' or face == 'y':
                faces.insert(i, face)
            elif face == 'q':
                print('quitting cube input...\n')
                faces = []
                break
            else:
                print('not a valid color.  Make sure that the input character was w, r, b, o, g, or y.\nTrying again...')
                i -= 1
            i += 1
    
    def printFaces(self):
        # Initialize a 9x12 2d list of characters.  These will represent the colors of 
        # the faces, with spaces wyere there is no face.
        _colors = []
        for y in range(9):
            _colors.insert(y, [])
            for x in range(12):
                _colors[y].insert(x, ' ')

        for face in self.faces:
            # insert top faces
            if face.wy == 2:
                _colors[face.ro + 1][face.bg + 4] = face.color
            # insert bottom faces
            elif face.wy == -2:
                _colors[-face.ro + 7][face.bg + 4] = face.color
            # insert front faces
            elif face.ro == 2:
                _colors[-face.wy + 4][face.bg + 4] = face.color
            # insert back faces
            elif face.ro == -2:
                _colors[-face.wy + 4][-face.bg + 10] = face.color
            # insert right faces
            elif face.bg == 2:
                _colors[-face.wy + 4][-face.ro + 7] = face.color
            # insert left faces
            elif face.bg == -2:
                _colors[-face.wy + 4][face.ro + 1] = face.color
        
        print('-------------------------')
        for y in range(9):
            print('|' + ' '.join(_colors[y]) + '|')
        print('-------------------------')
        return
    
    def scramble(self):
        for i in range(20):
            self.turn(randrange(1, 7), randrange(1, 4))