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
from defs import *

class Camera:
	def __init__(self):
		self.eye = Point3f(0.0, 0.0, 0.0)
		self.center = Point3f(0.0, 0.0, 0.0)
		self.up = Vector3f(0.0, 0.0, 0.0)

		self.fov = 45
		self.near = 0.1
		self.far = 10000
		self.cameraX = Vector3f(0.0, 0.0, 0.0)
		self.cameraY = Vector3f(0.0, 0.0, 0.0)
		self.cameraZ = Vector3f(0.0, 0.0, 0.0)

		self.createView( 	Point3f(0.0, 0.0, -10.0), \
							Point3f(0.0, 0.0, 0.0), \
							Vector3f(0.0, 1.0, 0.0) )

	def createView(self, eyePoint, centerPoint, upVector):
		self.eye = eyePoint
		self.orgEye = eyePoint

		self.center = centerPoint
		self.orgCenter = centerPoint

		self.up = upVector
		self.orgUp = upVector

		self.computeCamSpace()

	def setFov(self, f):
		self.fov = f

	def getFov(self):
		return self.fov

	def setNear(self, n):
		self.near = n

	def getNear(self):
		return self.near

	def setFar(self, f):
		self.far = f

	def getFar(self):
		return self.far

	def getEyePoint(self):
		return self.eye

	def getCenterPoint(self):
		return self.center

	def getUpVector(self):
		return self.up

	def setMouseMode(self, mode):
		self.mouseMode = mode

	def getMouseMode(self):
		return self.mouseMode

	def camDistance(self):
		view = self.eye - self.center
		return view.len()

	def preDolly(self, x, y, z):
		unCam = self.unRotateCam()
		traCam = Matrix.T(x, y, z)
		toCam = self.rotateCam()
		return Matrix.product3(unCam, traCam, toCam)

	def dolly(self, x, y, z):
		tx = self.preDolly(x, y, z)
		self.center = tx.vecmul(self.center)
		self.eye = tx.vecmul(self.eye)

	def zoom(self, z):
		tx = self.preDolly(0, 0, z)
		self.center = tx.vecmul(self.center)
		self.eye = tx.vecmul(self.eye)

	def dollyCamera(self, x, y, z):
		preViewVec = self.center - self.eye
		preViewVec = preViewVec.normalize()

		tx = self.preDolly(x, y, z)
		self.eye = tx.vecmul(self.eye)

		postViewVec = self.center - self.eye
		postViewVec = postViewVec.normalize()

		preViewVecYZ = Vector3f(0, preViewVec.y, preViewVec.z)
		preViewVecXZ = Vector3f(preViewVec.x, 0, preViewVec.z)
		postViewVecYZ = Vector3f(0, postViewVec.y, postViewVec.z)
		postViewVecXZ = Vector3f(postViewVec.x, 0, postViewVec.z)

		angleX = postViewVecYZ.angle(preViewVecYZ)
		angleY = postViewVecXZ.angle(preViewVecXZ)

		rot1 = Matrix.Rx(-angleX)
		rot2 = Matrix.Ry(-angleY)
		tmp1 = rot1.product(rot2)
		self.up = tmp1.vecmul(self.up)
		self.computeCamSpace()

	def dollyCenter(self, x, y, z):
		tx = self.preDolly(x, y, z)
		self.center = tx.vecmul(self.center)
		self.computeCamSpace()

	def pan(self, d):
		moveBack = Matrix.T(self.eye.x, self.eye.y, self.eye.z)
		rot = self.rotCamY(d)
		move = Matrix.T(-self.eye.x, -self.eye.y, -self.eye.z)

		tmp1 = Matrix.product3(moveBack, rot, move)

		self.center = tmp1.vecmul(self.center)
		self.up = tmp1.vecmul(self.up)

		self.computeCamSpace()

	def tilt(self, d):
		moveBack = Matrix.T(self.eye.x, self.eye.y, self.eye.z)
		rot = self.rotCamX(d)
		move = Matrix.T(-self.eye.x, -self.eye.y, -self.eye.z)

		tmp1 = Matrix.product3(moveBack, rot, move)

		self.center = tmp1.vecmul(self.center)
		self.up = tmp1.vecmul(self.up)

		self.computeCamSpace()

	def roll(self, d):
		moveBack = Matrix.T(self.eye.x, self.eye.y, self.eye.z)
		rot = self.rotCamZ(d)
		move = Matrix.T(-self.eye.x, -self.eye.y, -self.eye.z)

		tmp1 = Matrix.product3(moveBack, rot, move)

		self.center = tmp1.vecmul(self.center)
		self.up = tmp1.vecmul(self.up)

		self.computeCamSpace()

	def yaw(self, d):
		moveBack = Matrix.T(self.center.x, self.center.y, self.center.z)
		rot = self.rotCamY(d)
		move = Matrix.T(-self.center.x, -self.center.y, -self.center.z)

		tmp1 = Matrix.product3(moveBack, rot, move)

		self.eye = tmp1.vecmul(self.eye)
		self.up = tmp1.vecmul(self.up)

		self.computeCamSpace()

	def pitch(self, d):
		moveBack = Matrix.T(self.center.x, self.center.y, self.center.z)
		rot = self.rotCamX(d)
		move = Matrix.T(-self.center.x, -self.center.y, -self.center.z)

		tmp1 = Matrix.product3(moveBack, rot, move)

		self.eye = tmp1.vecmul(self.eye)
		self.up = tmp1.vecmul(self.up)

		self.computeCamSpace()

	def rotateCam(self):
		return Matrix.create(	[self.cameraX.x, self.cameraX.y, self.cameraX.z, 0.0, \
								self.cameraY.x, self.cameraY.y, self.cameraY.z, 0.0, \
								self.cameraZ.x, self.cameraZ.y, self.cameraZ.z, 0.0, \
								0.0, 0.0, 0.0, 1.0] )	

	def unRotateCam(self):
		return Matrix.create(	[self.cameraX.x, self.cameraY.x, self.cameraZ.x, 0.0, \
								self.cameraX.y, self.cameraY.y, self.cameraZ.y, 0.0, \
								self.cameraX.z, self.cameraY.z, self.cameraZ.z, 0.0, \
								0.0, 0.0, 0.0, 1.0] )	

	def rotCamX(self, a):
		unCam = self.unRotateCam()
		rotCam = Matrix.Rx(a)
		toCam = self.rotateCam()

		return Matrix.product3(unCam, rotCam, toCam)

	def rotCamY(self, a):
		unCam = self.unRotateCam()
		rotCam = Matrix.Ry(a)
		toCam = self.rotateCam()

		return Matrix.product3(unCam, rotCam, toCam)

	def rotCamZ(self, a):
		unCam = self.unRotateCam()
		rotCam = Matrix.Rz(a)
		toCam = self.rotateCam()

		return Matrix.product3(unCam, rotCam, toCam)

	def computeCamSpace(self):
		self.cameraZ = self.center - self.eye
		self.cameraZ = self.cameraZ.normalize()

		self.cameraX = self.cameraZ.cross(self.up)
		self.cameraX = self.cameraX.normalize()

		self.cameraY = self.cameraX.cross(self.cameraZ)
		#print self.cameraY, self.up

	def reset(self):
		self.eye = self.orgEye
		self.center = self.orgCenter
		self.up = self.orgUp
		self.computeCamSpace()



