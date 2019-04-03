# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019
from OpenGL.GL import *

# Since we use camera's transform to find final object positions 
# Camera class does not have much functionality, think about refactoring model3d draw method.
class Camera(object):
    
    def __init__(self, transform):
        self.transform = transform

    def __str__(self):
        return "Camera: " + self.transform