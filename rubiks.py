from cube import Cube
from cross import cross
from corners import corners

cube = Cube()
cube.input()
# cube.scramble()
cube.printFaces()
# cube.turn('r',1)
cross(cube)
corners(cube)
cube.printFaces()
