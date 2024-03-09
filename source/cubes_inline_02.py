# -*- coding: utf-8 -*-
"""
10 (3D) cubes laying in one line
The idea of the 10 cubes is that each cube represents a Natural number [0-9],
i.e. the last decimal value in any given Natural number.

Cubes are object oriented objects, with
- coordinates (x,y,z),
- size,
- color (same colour all sides)

prerequisite: pygame module
Install with one of the command below in a shell (command line window):
conda install cogsci::pygame
or
pip install pygame
Further info:: 
    https://www.pygame.org/wiki/GettingStarted
    https://www.pygame.org/docs/

Created on Thu Feb  8 18:14:53 2024
Last modified: 5 March 2024

@author: JOrban
"""

import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import sys
import math

class Cube:
    def __init__(self, color, x, y, z, size):
        self.color = color
        self.x = x
        self.y = y
        self.z = z
        self.size = size

    def draw(self):
        glDisable(GL_LIGHTING)  # Disable lighting to apply colors directly

        glBegin(GL_QUADS)

        glColor3fv(self.color)
        glVertex3f(self.x + self.size, self.y + self.size, self.z - self.size)
        glVertex3f(self.x - self.size, self.y + self.size, self.z - self.size)
        glVertex3f(self.x - self.size, self.y - self.size, self.z - self.size)
        glVertex3f(self.x + self.size, self.y - self.size, self.z - self.size)

        glVertex3f(self.x + self.size, self.y + self.size, self.z + self.size)
        glVertex3f(self.x - self.size, self.y + self.size, self.z + self.size)
        glVertex3f(self.x - self.size, self.y - self.size, self.z + self.size)
        glVertex3f(self.x + self.size, self.y - self.size, self.z + self.size)

        glVertex3f(self.x + self.size, self.y + self.size, self.z + self.size)
        glVertex3f(self.x - self.size, self.y + self.size, self.z + self.size)
        glVertex3f(self.x - self.size, self.y + self.size, self.z - self.size)
        glVertex3f(self.x + self.size, self.y + self.size, self.z - self.size)

        glVertex3f(self.x + self.size, self.y - self.size, self.z + self.size)
        glVertex3f(self.x - self.size, self.y - self.size, self.z + self.size)
        glVertex3f(self.x - self.size, self.y - self.size, self.z - self.size)
        glVertex3f(self.x + self.size, self.y - self.size, self.z - self.size)

        glVertex3f(self.x + self.size, self.y + self.size, self.z + self.size)
        glVertex3f(self.x + self.size, self.y + self.size, self.z - self.size)
        glVertex3f(self.x + self.size, self.y - self.size, self.z - self.size)
        glVertex3f(self.x + self.size, self.y - self.size, self.z + self.size)

        glVertex3f(self.x - self.size, self.y + self.size, self.z + self.size)
        glVertex3f(self.x - self.size, self.y + self.size, self.z - self.size)
        glVertex3f(self.x - self.size, self.y - self.size, self.z - self.size)
        glVertex3f(self.x - self.size, self.y - self.size, self.z + self.size)

        glEnd()

        glEnable(GL_LIGHTING)  # Enable lighting back after drawing

# Initialize Pygame and OpenGL
pygame.init()
display = (800, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("3D Cubes - real 3D") #software window title
# Set up perspective: https://pyopengl.sourceforge.net/documentation/manual-3.0/gluPerspective.html
gluPerspective(30, (display[0] / display[1]), 0.2, 100.0)

# Set up camera position and orientation
glTranslatef(0.0, 0, -10) # x,y,z set 50 for height max 3
glRotatef(30, 1, 0, 0)

cube_list = []

# Define colors
# BLACK   = (0, 0, 0) #background
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
GRAY    = (105, 105, 105)
COLORSET = [GRAY, RED, GREEN, BLUE, YELLOW] *2 #repeat for 10 cubes

positions = [(-2.7, 0), (-2.1, 0), (-1.5, 0), (-0.9, 0), (-0.3, 0),\
                 (0.3, 0), (0.9, 0), (1.5, 0), (2.1, 0), (2.7, 0)]

# Create cubes
for i in range(1,10,1):
    height = int(math.floor(i/10))*0.5 #new level created at every tenth number 
    last_digit = str(i)[-1]
    cube_list.append( Cube(COLORSET[i], positions[i%10][0], height, 0, 0.12)) #positions[position_index][1], 0.12) )

#wait window initialisation time
pygame.time.wait(200)

# Main loop
counter = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT|
            GL_DEPTH_BUFFER_BIT)
    # Draw cubes
    for i in range( min( len(cube_list), counter) ):       
        cube_list[i].draw()

    pygame.display.flip()
    pygame.time.wait(10) #may adjust appearence frequency of cubes

    counter += 1
