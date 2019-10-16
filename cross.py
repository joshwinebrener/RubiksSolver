from cube import Cube

def cross(cube):
    for face in cube.faces:
        # Select for white edge faces
        if face.color == 'w' \
            and (face.x == 0 or face.y == 0 or face.z == 0) \
            and ((face.x != 0 and face.y != 0) or (face.y != 0 and face.z != 0) or (face.x != 0 and face.z != 0)):
            # Find which side of the cross our face belongs to
                        
            # if the coordinate is 0, no need to change, if 1 or -1, turn to 2 or -2,
            # and if 2 or -2, turn to 1 or -1
            nextFace = [
                int(face.x * (2 if face.x == 1 or face.x == -1 else .5)),
                int(face.y * (2 if face.y == 1 or face.y == -1 else .5)),
                int(face.z * (2 if face.z == 1 or face.z == -1 else .5))
            ]
            openSide = [k.color for k in cube.faces if (k.x == nextFace[0] and k.y == nextFace[1] and k.z == nextFace[2])]
            if face.z > 1: currentSide = 'w'
            elif face.x > 1: currentSide = 'r'
            elif face.y > 1: currentSide = 'b'
            elif face.y < -1: currentSide = 'g'
            elif face.x < -1: currentSide = 'o'
            elif face.z < -1: currentSide = 'y'
            else: currentSide = '-'
            # print(currentSide)
            
            # Move white side to bottom layer
            # 2 clockwise turns if it is on the top
            if face.z > 1:
                cube.turn(currentSide, 2)
            

            else: raise NameError('cross error')

            # Twist bottom layer away
            # Undo the twist to the side that the piece came from
            # Align non-white side to correct center piece
            # Rotate correct center piece twice to insert white face
            # Repeat 4x