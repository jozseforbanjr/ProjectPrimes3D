# -*- coding: utf-8 -*-
"""
10 cubes laying in line, projected on a plane (parallel to one side)
The idea of the 10 cubes is that each cube represents a Natural number [0-9],
another way the last decimal value in any given number.

Cubes are object oriented (Cube class), with
- coordinates (x,y,z),
- size,
- color

prerequisite: pygame module
Install with one of the command below in a shell (command line window):
conda install cogsci::pygame
or
pip install pygame
Further info:: 
    https://www.pygame.org/wiki/GettingStarted
    https://www.pygame.org/docs/

@author: JOrban
Created on Wed Feb  7 22:50:46 2024
Last modified 05 March 2024
"""

import pygame
import sys

# Define colors
WHITE   = (255, 255, 255) #background
BLACK   = (0, 0, 0)
RED     = (255, 0, 0)
GREEN   = (0, 255, 0)
BLUE    = (0, 0, 255)
YELLOW  = (255, 255, 0)
GRAY    = (105, 105, 105)
COLORSET = [GRAY, RED, GREEN, BLUE, YELLOW] *2 #repeat for 10 cubes

# cube class definition
class Cube:
    def __init__(self, color, x, y, z, size):
        self.color = color
        self.x = x
        self.y = y
        self.z = z
        self.size = size

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    # Getter methods (not necessary)
    def get_color(self):
        return self.color

    def get_position(self):
        return (self.x, self.y, self.z)

    def get_size(self):
        return self.size

    # Setter methods
    def set_color(self, color):
        self.color = color

    def set_position(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def set_size(self, size):
        self.size = size

# Initialize pygame
pygame.init()

# Set the width and height of the screen [width, height]
#↨May be adjusted to monitor resolution but keep window edges in mind!
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D Cubes - projection") #software window title

# Create cubes
cubes = []
cube_size = 50
x_spacing = cube_size * 1.5 #spacing between cubes, higher than 1.5 needs to adjust view as well!

for i in range(10):
    #if you wish to have single colour, use this commented example:
    # cube = Cube(GRAY, 50 + i * x_spacing, 250, 0, cube_size)
    cube = Cube(COLORSET[i], 50 + i * x_spacing, 250, 0, cube_size)
    cubes.append(cube)

# Main loop, run until (user) quit
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill(WHITE)

    # Draw cubes
    for cube in cubes:
        cube.draw(screen)

    # Update the screen
    pygame.display.flip()
    pygame.time.wait(40) #adjust FPS
    
# Quit pygame
pygame.quit()
sys.exit()
