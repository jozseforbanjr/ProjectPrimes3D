# -*- coding: utf-8 -*-
"""
1 cube in 3D, rotating at its position

Cube is created as an object oriented object, with
- coordinates (x,y,z),
- size,
- color (all sides the same)

prerequisite: pygame module
Install with one of the command below in a shell (command line window):
conda install cogsci::pygame
or
pip install pygame
Further info:: 
    https://www.pygame.org/wiki/GettingStarted
    https://www.pygame.org/docs/

Created on Thu Feb  8 10:11:34 2024
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
glTranslatef(0, 0, -10) # x,y,z; set 10 
# Rotate cube: https://pyopengl.sourceforge.net/documentation/manual-3.0/glRotate.html
glRotatef(30, 1, 0, 0) # angle , x , y , z 
height      = 0
cube_list   = []

# Define colors (R, G, B)
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
GRAY    = (105, 105, 105)
WHITE  = (255, 255, 255)

positions = [(0, 0)]

cube_list.append( Cube(WHITE, positions[0][0], height, 0, 0.12))

#wait window initialisation time
pygame.time.wait(200)

# Main loop
counter = 1
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    glRotatef(1,1,2,-1)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT|
            GL_DEPTH_BUFFER_BIT)
    # Draw cubes
    cube_list[0].draw()

    pygame.display.flip()
    pygame.time.wait(10) #may adjust draw frequency of cube

    counter += 1
