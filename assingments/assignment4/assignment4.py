# CENG 487 Assignment4 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 05-2019
import sys
import numpy
import math

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from vector import *
from matrix import *
from shapes import *
from camera import *
from scene import *
from view import *

if len(sys.argv) != 2:
    print(".obj file is missing!\nusage: python assignment3.py <objectname>.obj")
    sys.exit()

# create grid
grid = Grid("grid", 10, 10)
grid.setDrawStyle(DrawStyle.WIRE)
grid.setWireWidth(1)

# create camera
camera = Camera()
camera.createView( 	Point3f(0.0, 0.0, 10.0), \
					Point3f(0.0, 0.0, 0.0), \
					Vector3f(0.0, 1.0, 0.0) )
camera.setNear(1)
camera.setFar(1000)

# create View
view = View(camera, grid)

# init scene
scene = Scene()
view.setScene(scene)

# create objects
shape = Shape(sys.argv[1])
scene.add(shape)

def main():
	global view
	glutInit(sys.argv)

	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)

	glutInitWindowSize(640, 480)
	glutInitWindowPosition(200, 200)

	window = glutCreateWindow("CENG487 Assigment Template")

	# define callbacks
	glutDisplayFunc( view.draw )
	glutIdleFunc( view.idleFunction )
	glutReshapeFunc( view.resizeView ) 
	glutKeyboardFunc( view.keyPressed )
	glutSpecialFunc( view.specialKeyPressed )
	glutMouseFunc( view.mousePressed )
	glutMotionFunc( view.mouseMove )

	# Initialize our window
	width = 640
	height = 480
	glClearColor(0.0, 0.0, 0.0, 0.0)	# This Will Clear The Background Color To Black
	glClearDepth(1.0)					# Enables Clearing Of The Depth Buffer
	glDepthFunc(GL_LEQUAL)				# The Type Of Depth Test To Do
	glEnable(GL_DEPTH_TEST)				# Enables Depth Testing
	#glEnable(GL_LINE_SMOOTH)			# Enable line antialiasing
	glShadeModel(GL_SMOOTH)				# Enables Smooth Color Shading
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()					# Reset The Projection Matrix

	# create the perpective projection
	gluPerspective( view.camera.fov, float(width)/float(height), camera.near, camera.far )
	glMatrixMode(GL_MODELVIEW)

	# Start Event Processing Engine	
	glutMainLoop()

# Print message to console, and kick off the main to get it rolling.
print("Hit ESC key to quit.")
main()
		
