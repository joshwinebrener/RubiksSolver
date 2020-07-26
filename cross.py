from cube import Cube

def cross(cube):
    for face in cube.faces:
        if face.isEdgePiece() and face.color == 'w': # Filter for white edge pieces
            if face.z == 2: # face is already on white side
                if not cube.sisterFaces(face).onCorrectSide():
                    # Rotate face to the yellow side if doesn't match
                    cube.turn(face.adjacentSide(), 2)
                    # Follow yellow side procedure once face is on yellow side
                    while (not cube.sisterFaces(face).onCorrectSide()):
                        cube.turn ('y', 1)
                    cube.turn(face.adjacentSide(), 2)
            elif face.z == -2: # face is on yellow side
                while (not cube.sisterFaces(face).onCorrectSide()):
                    cube.turn ('y', 1)
                cube.turn(face.adjacentSide(), 2)
            else: # face on red, blue, orange, or green side
                front = face.currentSide()
                frontReset = 0
                # Get the face to the middle plane if it isn't there already.
                if abs(face.z) == 1:
                    cube.turn(front, 1)
                    frontReset = -1
                adjacent = face.adjacentSide()
                adjacentReset = 0
                while face.currentSide() != 'y':
                    cube.turn(adjacent, 1)
                    adjacentReset -= 1
                cube.turn('y', 2)
                cube.turn(adjacent, adjacentReset)
                if frontReset != 0:
                    cube.turn(front, frontReset)
                # Follow yellow side procedure once face is on yellow side
                while (not cube.sisterFaces(face).onCorrectSide()):
                    cube.turn ('y', 1)
                cube.turn(face.adjacentSide(), 2)
    return