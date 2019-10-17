from cube import Cube

def cross(cube):
    for face in cube.faces:
        # Select for white edge faces
        if face.color == 'w' \
            and (face.bg == 0 or face.ro == 0 or face.wy == 0) \
            and ((face.bg != 0 and face.ro != 0) or (face.ro != 0 and face.wy != 0) or (face.bg != 0 and face.wy != 0)):
            # Find which side of the cross our face belongs to
                        
            # if the coordinate is 0, no need to change, if 1 or -1, turn to 2 or -2,
            # and if 2 or -2, turn to 1 or -1
            nextFace = [
                int(face.bg * (2 if face.bg == 1 or face.bg == -1 else .5)),
                int(face.ro * (2 if face.ro == 1 or face.ro == -1 else .5)),
                int(face.wy * (2 if face.wy == 1 or face.wy == -1 else .5))
            ]
            openSide = [k.color for k in cube.faces if (k.bg == nextFace[0] and k.ro == nextFace[1] and k.wy == nextFace[2])]
            if face.wy > 1: currentSide = 'w'
            elif face.bg > 1: currentSide = 'r'
            elif face.ro > 1: currentSide = 'b'
            elif face.ro < -1: currentSide = 'g'
            elif face.bg < -1: currentSide = 'o'
            elif face.wy < -1: currentSide = 'y'
            else: currentSide = '-'
            # print(currentSide)
            
            # Move white side to bottom layer
            # 2 clockwise turns if it is on the top
            if face.wy > 1:
                cube.turn(currentSide, 2)
            

            else: raise NameError('cross error')

            # Twist bottom layer away
            # Undo the twist to the side that the piece came from
            # Align non-white side to correct center piece
            # Rotate correct center piece twice to insert white face
            # Repeat 4x