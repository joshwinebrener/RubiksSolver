from cube import Cube
from cross import cross

cube = Cube()
cube.printFaces()
# cube.input()
cube.scramble()
# cube.turn('r',1)
cross(cube)
cube.printFaces()
