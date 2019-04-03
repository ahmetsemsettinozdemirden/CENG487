# CENG 487 Assignment3 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 04-2019

# References:
# https://stackoverflow.com/questions/628796/what-does-glloadidentity-do-in-opengl
# http://www.songho.ca/opengl/gl_projectionmatrix.html
# http://www.opengl-tutorial.org/beginners-tutorials/tutorial-3-matrices/
# https://www.khronos.org/registry/OpenGL-Refpages/gl2.1/xhtml/glPushMatrix.xml
# http://makble.com/opengl-matrix-stacks-and-current-matrix
# https://www.glprogramming.com/red/chapter03.html
# https://learnopengl.com/Getting-started/Camera

import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from scene.mainscene import MainScene
from factory.camerafactory import CameraFactory
from camera import Camera

ESCAPE = '\033'
window = 0

if len(sys.argv) != 2:
    print(".obj file is missing!\nusage: python assignment3.py <objectname>.obj")
    sys.exit()

# Main Scene
mainScene = MainScene()
mainScene.init(sys.argv[1])

def InitGL(Width, Height):
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glDepthFunc(GL_LESS)
    glEnable(GL_DEPTH_TEST)
    glShadeModel(GL_SMOOTH)
	
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)

    glMatrixMode(GL_MODELVIEW)

def ReSizeGLScene(Width, Height):
    if Height == 0: 
	    Height = 1

    glViewport(0, 0, Width, Height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, float(Width)/float(Height), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)

def DrawGLScene():
	global mainScene

	# === Update ===
	mainScene.update()

	# === Render ===
	# Clear the screen
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
	# Render scene
	mainScene.render()
	glutSwapBuffers()

def keyPressed(*args):
    global mainScene
    mainScene.keyPressed(args[0])
    if args[0] == ESCAPE:
        sys.exit()

def specialKeyPressed(key, x, y):
    # since i dont want my main scene is dependent to glut, i converted GLUT_KEY_LEFT to LEFT_ARROW and so on.
    global mainScene
    if key == GLUT_KEY_LEFT:
        mainScene.keyPressed('LEFT_ARROW')
    elif key == GLUT_KEY_RIGHT:
        mainScene.keyPressed('RIGHT_ARROW')
    if key == GLUT_KEY_UP:
        mainScene.keyPressed('UP_ARROW')
    elif key == GLUT_KEY_DOWN:
        mainScene.keyPressed('DOWN_ARROW')

def main():
	global window
	glutInit(sys.argv)
	glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
	glutInitWindowSize(640, 480)
	glutInitWindowPosition(0, 0)

	window = glutCreateWindow("Sems3d")
	glutDisplayFunc(DrawGLScene)
	#glutFullScreen()
	glutIdleFunc(DrawGLScene)
	glutReshapeFunc(ReSizeGLScene)
	glutKeyboardFunc(keyPressed)
	glutSpecialFunc(specialKeyPressed)
	InitGL(640, 480)
	glutMainLoop()

print("Hit ESC key to quit.\nUse arrow keys to rotate object.\nUse +/- to apply subdivision on object.\nHit 'r' to reset object transformation.\nHave fun!")
main()