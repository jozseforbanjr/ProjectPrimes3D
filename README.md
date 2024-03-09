# ProjectPrimes3D
Projecting prime numbers in space for visualization

Presenting Prime numbers as coloured cubes on a "Decimal Wall of Natural Numbers".
I refer as "Decimal Wall of Natural Numbers" to such a table-like representation 
of Natural numbers in which in each line there are 10 positions.
Each position refers to the last decimal value in a given number [0-9]. Reaching every tenth
number a new line is created (above the previous). In this code counting goes up to 1000.
Only Prime numbers are coloured, with different colours respectively to their position in the wall,
i.e. depending on the last digit.
Non-Prime numbers are represented by gray cubes.
The wall is built "brick-by-brick", with a simple animation.

Cubes are object oriented objects, with
- coordinates (x,y,z)
- size
- color (all sides the same)

prerequisite: pygame module
Install with one of the command below in a shell (command line window):
conda install cogsci::pygame
or
pip install pygame
Further info:: 
    https://www.pygame.org/wiki/GettingStarted
    https://www.pygame.org/docs/

***************************
source folder: Python codes

"..\source\cubes_inline.py" - 10 coloured cubes laying in line, projected on a plane (parallel to one side). It was an initial try of demonstration, which was rejected as a solution because it is only a projection, not a real 3D object
"..\source\cube3D.py" - one single (3D) cube as building brick of the wall, rotating at its position. Later on rotation is neglected, here it rotates only for demonstration purpose.
"..\source\cubes_inline_02.py" - 10 (3D) cubes laying in one line. The idea of the 10 cubes is that each cube represents a Natural number [0-9], i.e. the last decimal value in any given Natural number.
"..\source\primes_wall_01.py" - Wall of Prime numbers (up to 1000). 3D cubes lined up in rows of 10 cubes.

***************************
images folder: imaged of created demonstrations

"..\images\10colouredCubes.png" and
"..\images\10grayCubes.png" - are made by projection of cubes on one plane (parallel to a cube side), cubes_inline.py 
"..\images\10colouredCubes_2.png" - is made as 10 real 3D cubes in line, cubes_inline_02.py
"..\images\rotating_WhiteCube.gif" - 3D (white) cube rotationg, made by cube3D.py
"..\images\WallOfPrimes_01.png" - Prime numbers (up to 1000) represented in a wall of all Natural numbers, made by primes_wall_01.py

Last modified: 8 March 2024
