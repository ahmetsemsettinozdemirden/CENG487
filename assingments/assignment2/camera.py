# CENG 487 Assignment2 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019
from OpenGL.GL import *

class Camera(object):

    def __init__(self, transform):
        self.transform = transform

    def __str__(self):
        return "Camera: " + self.transform

    def update(self):
    	self.transform.update()
        # Reset The View 
        glLoadIdentity()
        # move camera and render the world according to that position
        glTranslatef(self.transform.position.x, self.transform.position.y, self.transform.position.z)