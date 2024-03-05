# -*- coding: utf-8 -*-
"""
Presenting Prime nummbers as coloured cubes on a "Decimal Wall of Natural Numbers".
Only Prime numbers are coloured, with different colours respectively to their position in the wall,
i.e. depending on the last digit.
Non-Prime numbers are represented by gray cubes.
The wall is built "brick-by-brick", with a simple animation.

Cubes are object oriented objects, with
- coordinates (x,y,z)
- size
- color

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
display = (400, 600)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
pygame.display.set_caption("Wall of Primes (1-1000)") #software window title
# Set up perspective: https://pyopengl.sourceforge.net/documentation/manual-3.0/gluPerspective.html
gluPerspective(30, (display[0] / display[1]), 0.2, 100.0)

# Set up camera position and orientation
glTranslatef(0.0, -24.0, -100) # x,y,z set 50 for height max 3
glRotatef(30, 1, 0, 0)

cube_list = []

positions = [(-2.7, 0), (-2.1, 0), (-1.5, 0), (-0.9, 0), (-0.3, 0),\
                 (0.3, 0), (0.9, 0), (1.5, 0), (2.1, 0), (2.7, 0)]

#skipping 2 and 5 from list of primes
primes_list = [3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97,
               101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199,
               211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293,
               307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397,
               401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499,
               503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599,
               601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691,
               701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797,
               809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887,
               907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997]

# Create cubes
for i in range(1,1000,1):
    
    if False: #magasság az értékkel arányosan növekszik
        height = i/20 #int(math.floor(math.log10(current_number)))
    if True: #10-es osztályszintek
        height = int(math.floor(i/10))*0.5
    # radius = 10/1000*current_number # math.sqrt(10**height)
    # positions = Circle.calculate_positions(4) #10**(height+1)-10**height)
    
    
    # factor = 0.5*(h%10)/10
    # color = (0.4+factor, 0.4+factor, 0.4+factor)
    
    # if h == 0:
    #     color = (1, 1, 1)
    # elif h == 1: 
    #     color = (0, 0, 1)
    # else:
    #     color = (0, 1, 0)
    # for i in range(4):
        # current_number = h*10 + i
    
    last_digit = str(i)[-1]
    
    if i in set(primes_list):
        # color = (0.5, 0.5, 0.5)
        # if (h*10 + i) == 101:
        
        if last_digit == '1':
            color = (1, 1, 1)
            position_index = 0
        elif last_digit == '3':
            color = (0, 1, 0)
            position_index = 1
        elif last_digit == '7':
            color = (1, 0, 0) #red
            position_index = 2
        elif last_digit == '9':
            color = (0, 0, 1) #blue
            position_index = 3
        
    else:
        color = (0.3, 0.3, 0.3)
        if last_digit == '1':
            
            position_index = 0
        elif last_digit == '3':
            
            position_index = 1
        elif last_digit == '7':
            
            position_index = 2
        elif last_digit == '9':
            
            position_index = 3   
        
        # cube2 = Cube((0, 1, 0), -2**0.5, 2**0.5, 0, 1)
        # cube3 = Cube((0, 0, 1), 2**0.5, 2**0.5, 0, 1)
        # cube4 = Cube((1, 1, 0), 2**0.5, -2**0.5, 0, 1)
    # print(str(i) + '# ' + str(i) + ' ('+ str(last_digit) + '), pos_idx: ' +  str(i%10) + ', pos: ' + str(positions[i%10]))
    cube_list.append( Cube(color, positions[i%10][0], height, 0, 0.12)) #positions[position_index][1], 0.12) )
    # cube_list.append( Cube(color, radius*positions[current_number-10**height][0], 3/1000*current_number, radius*positions[current_number-10**height][1], 0.12) )
    # cube_list.append( Cube(color, radius*positions[position_index][0], 3/1000*current_number, radius*positions[position_index][1], 0.12) )

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
    #NEM KELL FORGATNI
    # glRotatef(1,0,2,-1) #rotation matrix (angle,x,y,z)
    # glRotatef(1,0,1,0) #rotation matrix (angle,x,y,z)
    glEnable(GL_DEPTH_TEST)
    glClear(GL_COLOR_BUFFER_BIT|
            GL_DEPTH_BUFFER_BIT)
    # Draw cubes
    for i in range( min( len(cube_list), counter) ):       
        cube_list[i].draw()
    # cube1.draw()
    # cube2.draw()
    # cube3.draw()
    # cube4.draw()

    pygame.display.flip()
    pygame.time.wait(10) #may adjust appearence frequency of cubes

    counter += 1
