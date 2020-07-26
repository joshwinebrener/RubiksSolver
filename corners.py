from cube import Cube

def corners(cube):
    for face in cube.faces:
        if face.color == 'w' and face.isCornerPiece():
            # Get the face to z = -1
            if face.z > 0:
                if face.currentSide() == 'w':
                    adj = face.rightAdjacent()
                    cube.turn(adj, 1)
                    cube.turn('y', 1)
                    cube.turn(adj, -1)
                else:
                    adj = face.currentSide()
                    direction = -1 if face.rightAdjacent() == 'w' else 1
                    cube.turn(adj, direction)
                    cube.turn('y', direction)
                    cube.turn(adj, -direction)
            elif face.z == -2:
                while cube.at(face.x, face.y, 2).color == 'w':
                    cube.turn('y', 1)
                adj = face.rightAdjacent()
                cube.turn(adj, -1)
                cube.turn('y', 1)
                cube.turn(adj, 1)
            # insert the piece.  By this point, z == -1
            sister1 = cube.sisterFaces(face)[0]
            sister2 = cube.sisterFaces(face)[1]
            bottomColor = sister1.color if sister1.z == -2 else sister2.color
            while face.currentSide() != bottomColor:
                cube.turn('y', 1)
            adj = face.currentSide()
            direction = 1 if face.rightAdjacent() == 'y' else -1
            cube.turn(adj, direction)
            cube.turn('y', direction)
            cube.turn(adj, -direction)
    return