# CENG 487 Assignment4 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 05-2019
import random
import copy

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

from math import pi,sin,cos,sqrt,acos
from vector import *
from matrix import *
from boundingbox import *
from defs import DrawStyle

__all__ = ['_Shape', 'Cube', 'DrawStyle', 'Shape']

class _Shape:
	def __init__(self, name, vertices, faces):
		self.vertices = vertices
		self.edges = []
		self.faces = faces
		self.colors = []
		self.obj2World = Matrix()
		self.drawStyle = DrawStyle.NODRAW
		self.wireOnShaded = False
		self.wireWidth = 2
		self.name = name
		self.fixedDrawStyle = False
		self.wireColor = ColorRGBA(0.7, 1.0, 0.0, 1.0)
		self.wireOnShadedColor = ColorRGBA(1.0, 1.0, 1.0, 1.0)
		self.bboxObj = BoundingBox()
		self.bboxWorld = BoundingBox()
		self.calcBboxObj()

	def calcBboxObj(self):
		for vertex in self.vertices:
			self.bboxObj.expand(vertex)

	def setDrawStyle(self, style):
		self.drawStyle = style

	def setWireColor(self, r, g, b, a):
		self.wireColor = ColorRGBA(r, g, b, a)

	def setWireWidth(self, width):
		self.wireWidth = width

	def draw(self):
		index = 0
		for face in self.faces:
			if self.drawStyle == DrawStyle.FACETED or self.drawStyle == DrawStyle.SMOOTH:
				glBegin(GL_POLYGON)

				if len(self.colors) > 0:
					glColor3f(self.colors[index].r, self.colors[index].g, self.colors[index].b)
				else:
					glColor3f(1.0, 0.6, 0.0)

				for vertex in face:
					glVertex3f(self.vertices[vertex].x, self.vertices[vertex].y, self.vertices[vertex].z)
				glEnd()

			if self.drawStyle == DrawStyle.WIRE or self.wireOnShaded == True:
				glPolygonMode( GL_FRONT_AND_BACK, GL_LINE )
				glLineWidth(self.wireWidth)
				#glDisable(GL_LIGHTING)
				
				glBegin(GL_POLYGON)

				if self.wireOnShaded == True:
					if self.fixedDrawStyle == True:
						glColor3f(self.wireColor.r, self.wireColor.g, self.wireColor.b)
					else:
						glColor3f(self.wireOnShadedColor.r, self.wireOnShadedColor.g, self.wireOnShadedColor.b)
				else:
					glColor3f(self.wireColor.r, self.wireColor.g, self.wireColor.b)

				for vertex in face:
					glVertex3f(self.vertices[vertex].x, self.vertices[vertex].y, self.vertices[vertex].z)
				glEnd()

				glPolygonMode( GL_FRONT_AND_BACK, GL_FILL )
				#glEnable(GL_LIGHTING)

			index += 1

	def Translate(self, x, y, z):
		translate = Matrix.T(x, y, z)
		self.obj2World = self.obj2World.product(translate)

	def subdivide(self):
		"""
		self.vertices = [ Point3f(1.0, 1.0, 1.0), ...]
		self.faces = [ [0, 2, 3, 1], ...]

		references:
		- https://en.wikipedia.org/wiki/Catmull%E2%80%93Clark_subdivision_surface
		- http://www.rorydriscoll.com/2008/08/01/catmull-clark-subdivision-the-basics/
		- https://rosettacode.org/wiki/Catmull%E2%80%93Clark_subdivision_surface
		- https://www.algosome.com/articles/catmull-clark-subdivision-algorithm.html
		"""
		vertices = copy.deepcopy(self.vertices)
		faces = copy.deepcopy(self.faces)
		
		# 1. face points
		facePoints = [reduce(lambda v1, v2: v1 + v2, map(lambda idx: self.vertices[idx], face)) * (1.0/len(face)) for face in faces]

		# 2. find edges
		edges = []

		# get edges from each face
		for faceIndex in range(len(faces)):
			face = faces[faceIndex]
			faceLength = len(face)

			for pointNumIndex in range(faceLength):
				# if not last point then edge is curr point and next point, else edge is curr point and first point
				pointNum1 = face[pointNumIndex]
				pointNum2 = face[pointNumIndex + 1 if (pointNumIndex < faceLength - 1) else 0]

				# order points in edge by lowest point number
				if pointNum1 > pointNum2:
					pointNum1, pointNum2 = pointNum2, pointNum1

				edges.append([pointNum1, pointNum2, faceIndex])

		# sort edges by pointNum1, pointNum2, faceIndex
		edges = sorted(edges)
	
		# merge edges with 2 adjacent faces
		# [pointNum1, pointNum2, faceIndex1, faceIndex2]
		mergedEdges = []
 
		for edgeIndex in range(len(edges) / 2):
			edge1 = edges[2 * edgeIndex]
			edge2 = edges[2 * edgeIndex + 1]
			mergedEdges.append([edge1[0], edge1[1], edge1[2], edge2[2]])
 
    # add edge centers
		# [pointNum1, pointNum2, faceIndex1, faceIndex2, centerPoint]
		edgesCenters = []
	
		for mergedEdge in mergedEdges:
			point1 = vertices[mergedEdge[0]]
			point2 = vertices[mergedEdge[1]]
			centerPoint = (point1 + point2) * 0.5
			edgesCenters.append(mergedEdge + [centerPoint])

		# 3. edge points
		edgePoints = []

		for edgeFace in edgesCenters:
			# get center of edge
			centerEdgePoint = edgeFace[4]
			# get center of two facepoints
			facePoint1 = facePoints[edgeFace[2]]
			facePoint2 = facePoints[edgeFace[3]]
			centerFacePoint = (facePoint1 + facePoint2) * 0.5
			# get average between center of edge and center of facepoints
			edgePoint = (centerEdgePoint + centerFacePoint) * 0.5
			edgePoints.append(edgePoint)      
 
		# 4. new vertices

		# 4.1 average face points
		# the average of the face points of the faces the point belongs to (avg_face_points)
		tempPoints = []					# [[Point3f(0.0, 0.0, 0.0), 0], ...]
		averageFacePoints = []  # [Point3f(0.0, 0.0, 0.0), ...]
		for pointIndex in range(len(vertices)):
			tempPoints.append([Point3f(0.0, 0.0, 0.0), 0])
 
    # loop through faces updating tempPoints
		for faceIndex in range(len(faces)):
			for pointIndex in faces[faceIndex]:
				tempPoints[pointIndex][0] = tempPoints[pointIndex][0] + facePoints[faceIndex]
				tempPoints[pointIndex][1] += 1
 
    # divide to create avg_face_points
		for tempPoint in tempPoints:
			averageFacePoints.append(tempPoint[0] * (1.0/tempPoint[1]))

    # 4.2 average mid edges
		# the average of the centers of edges the point belongs to (avg_mid_edges)
		tempPoints = []					# [[Point3f(0.0, 0.0, 0.0), 0], ...]
		averageMidEdges = []		# [Point3f(0.0, 0.0, 0.0), ...]
		for pointIndex in range(len(vertices)):
			tempPoints.append([Point3f(0.0, 0.0, 0.0), 0])

		# go through edgesCenters using center updating each point
		for edge in edgesCenters:
			for pointIndex in [edge[0], edge[1]]:
				tempPoints[pointIndex][0] = tempPoints[pointIndex][0] + edge[4]
				tempPoints[pointIndex][1] += 1

		# divide out number of points to get average
		for tempPoint in tempPoints:
			averageMidEdges.append(tempPoint[0] * (1.0/tempPoint[1]))

		# 4.3 point faces
		# how many faces a point belongs to
		pointsFaces = []

		for pointIndex in range(len(vertices)):
			pointsFaces.append(0)

		# loop through faces updating pointsFaces
		for faceIndex in range(len(faces)):
			for pointIndex in faces[faceIndex]:
				pointsFaces[pointIndex] += 1

		# 4.4 new vertices with barycenter
		"""
		m1 = (n - 3) / n
		m2 = 1 / n
		m3 = 2 / n
		newCoords = (m1 * oldCoords) + (m2 * averageFacePoints) + (m3 * averageMidEdges)
		"""
		newVertices = []

		for pointIndex in range(len(vertices)):
			n = pointsFaces[pointIndex]
			m1 = (n - 3.0) / n
			m2 = 1.0 / n
			m3 = 2.0 / n
			newCoords = (m1 * vertices[pointIndex]) + (m2 * averageFacePoints[pointIndex]) + (m3 * averageMidEdges[pointIndex])
			newVertices.append(newCoords)

		# 4.5 add face points to newVertices
		facePointIndices = []
		edgePointIndices = dict()
		nextPointIndex = len(newVertices)

		# point num after next append to newVertices
		for facePoint in facePoints:
			newVertices.append(facePoint)
			facePointIndices.append(nextPointIndex)
			nextPointIndex += 1
 
		# add edge points to newPoints
		for edgeIndex in range(len(edgesCenters)):
			pointIndex1 = edgesCenters[edgeIndex][0]
			pointIndex2 = edgesCenters[edgeIndex][1]
			edgePoint = edgePoints[edgeIndex]
			newVertices.append(edgePoint)
			edgePointIndices[(pointIndex1, pointIndex2)] = nextPointIndex
			nextPointIndex += 1

		# 5. new faces 
		# newVertices now has the points to output. Need new faces
		newFaces = []

		for oldFaceIndex in range(len(faces)):
			oldFace = faces[oldFaceIndex]
			# 4 point face
			if len(oldFace) == 4:
  			# old vertices
				a = oldFace[0]
				b = oldFace[1]
				c = oldFace[2]
				d = oldFace[3]
				# create face point and edges
				facePoint_abcd = facePointIndices[oldFaceIndex]
				edge_point_ab = edgePointIndices[self.sortIndices((a, b))]
				edge_point_da = edgePointIndices[self.sortIndices((d, a))]
				edge_point_bc = edgePointIndices[self.sortIndices((b, c))]
				edge_point_cd = edgePointIndices[self.sortIndices((c, d))]
				# add new faces
				newFaces.append((a, edge_point_ab, facePoint_abcd, edge_point_da))
				newFaces.append((b, edge_point_bc, facePoint_abcd, edge_point_ab))
				newFaces.append((c, edge_point_cd, facePoint_abcd, edge_point_bc))
				newFaces.append((d, edge_point_da, facePoint_abcd, edge_point_cd))  
			else:
				raise "face is broken!"

		# 6. assign new shape
		self.vertices = newVertices
		self.faces = newFaces
		self.colors = []
		for i in range (0, len(newFaces) + 1):
			r = random.uniform(0, 1)
			g = random.uniform(0, 1)
			b = random.uniform(0, 1)
			self.colors.append( ColorRGBA(r, g, b, 1.0) )

	def sortIndices(self, indices):
		return indices if indices[0] < indices[1] else (indices[1], indices[0])

class Cube(_Shape):
	def __init__(self, name, xSize, ySize, zSize, xDiv, yDiv, zDiv):
		vertices = []
		xStep = xSize / (xDiv + 1.0)
		yStep = ySize / (yDiv + 1.0)
		zStep = zSize / (zDiv + 1.0)
		# for i in range(0, xDiv):
		# 	for j in range(0, yDiv):
		# 		for k in range(0, zDiv):
		# 			x = -xSize / 2.0 + i * xStep
		# 			y = -ySize / 2.0 + j * yStep
		# 			z = -zSize / 2.0 + k * zStep
		# 			vertices.append( Point3f(x, y, z) )
		#add corners
		vertices.append( Point3f(-xSize / 2.0, -ySize / 2.0, zSize / 2.0) )
		vertices.append( Point3f(xSize / 2.0, -ySize / 2.0, zSize / 2.0) )
		vertices.append( Point3f(-xSize / 2.0, ySize / 2.0, zSize / 2.0) )
		vertices.append( Point3f(xSize / 2.0, ySize / 2.0, zSize / 2.0) )
		vertices.append( Point3f(-xSize / 2.0, -ySize / 2.0, -zSize / 2.0) )
		vertices.append( Point3f(xSize / 2.0, -ySize / 2.0, -zSize / 2.0) )
		vertices.append( Point3f(-xSize / 2.0, ySize / 2.0, -zSize / 2.0) )
		vertices.append( Point3f(xSize / 2.0, ySize / 2.0, -zSize / 2.0) )

		faces = []
		faces.append( [0, 2, 3, 1] )
		faces.append( [4, 6, 7, 5] )
		faces.append( [4, 6, 2, 0] )
		faces.append( [1, 3, 7, 5] )
		faces.append( [2, 6, 7, 3] )
		faces.append( [4, 0, 1, 5] )

		_Shape.__init__(self, name, vertices, faces)
		self.drawStyle = DrawStyle.SMOOTH

		for i in range (0, len(faces) + 1):
			r = random.uniform(0, 1)
			g = random.uniform(0, 1)
			b = random.uniform(0, 1)
			self.colors.append( ColorRGBA(r, g, b, 1.0) )

class Shape(_Shape):
  
	def __init__(self, objDest):
		vertices = []
		faces = []

		# read file and get rid of '\n' at the end of each line.
		with open(objDest) as f:
				lines = f.readlines()
				name = f.name
		lines = [line.strip() for line in lines] 

		# parse vertices
		for line in lines:
				if line != '' and line[0] is 'v':
						vertexLine = line.split(' ')
						# create vertex
						vertices.append(Point3f(float(vertexLine[1]), 
																		float(vertexLine[2]),
																		float(vertexLine[3])))
		
		# parse faces
		for line in lines:
				if line != '' and line[0] is 'f':
						# find vertex indices
						faceElements = [(int(e) - 1) for e in line.split(' ')[1:]] # TODO: (int(e) - 1)
						faces.append(faceElements)

		_Shape.__init__(self, name, vertices, faces)
		self.drawStyle = DrawStyle.SMOOTH

		for i in range (0, len(faces) + 1):
			r = random.uniform(0, 1)
			g = random.uniform(0, 1)
			b = random.uniform(0, 1)
			self.colors.append( ColorRGBA(r, g, b, 1.0) )
