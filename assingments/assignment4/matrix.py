# CENG 487 Assignment4 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 05-2019
from math import pi,sin,cos,sqrt,acos
from vector import *
import numpy

class Matrix:
	@staticmethod
	def create(arg):
		if len(arg) != 16:
			raise Exception("array size must be 16!")
		cols = []
		for x in range(0, 4):
			cols.append(HCoord(arg[x], arg[x + 4], arg[x + 8], arg[x + 12]))
		return Matrix(cols)

	def __init__(self, cols = None):
		if cols is None:
			self.cols = [HCoord(1.0, 0.0, 0.0, 0.0), HCoord(0.0, 1.0, 0.0, 0.0), HCoord(0.0, 0.0, 1.0, 0.0), HCoord(0.0, 0.0, 0.0, 1.0)]
		else:
			self.cols = cols

		self.rows = self.createrows()

	def __str__(self):
		string = ""
		for x in self.cols:
			string += str(x) + "\n"
		return string

	def asList(self):
		result = []
		for column in self.cols:
			result.append(column.x)
			result.append(column.y)
			result.append(column.z)
			result.append(column.w)

		return result

	def asNumpy(self):
		result = []
		for column in self.cols:
			result.append([column.x, column.y, column.z, column.w]) 

		return numpy.asarray(result)

	def createrows(self):
		x = HCoord(self.cols[0].x, self.cols[1].x, self.cols[2].x, self.cols[3].x)
		y = HCoord(self.cols[0].y, self.cols[1].y, self.cols[2].y, self.cols[3].y)
		z = HCoord(self.cols[0].z, self.cols[1].z, self.cols[2].z, self.cols[3].z)
		w = HCoord(self.cols[0].w, self.cols[1].w, self.cols[2].w, self.cols[3].w)
		return [x, y, z, w]

	def trans(self):
		return Matrix(self.rows)

	def rowsize(self):
		return len(self.rows)

	def colsize(self):
		return len(self.cols)

	def vecmul(self, vector):
		x = self.cols[0] * vector.x
		y = self.cols[1] * vector.y
		z = self.cols[2] * vector.z
		w = self.cols[3] * vector.w
		return x + y + z + w

	def product(self, other):
		cols = []
		for x in xrange(0, other.colsize()):
			cols.append(self.vecmul(other.cols[x]))
		return Matrix(cols)

	@staticmethod
	def product3(mat1, mat2, mat3):
		tmp = mat1.product(mat2)
		return tmp.product(mat3)

	def __add__(self, other):
		cols = []
		for x in xrange(0, self.colsize()):
			cols.append(self.cols[x] + other.cols[x])
		return Matrix(cols)

	def __mul__(self, scalar):
		cols = map(lambda x: scalar * x,self.cols)
		return Matrix(cols)

	def __rmul__(self, scalar):
		return self.__mul__(scalar)

	@staticmethod
	def Rx(x):
		return Matrix.create([1.0, 0.0, 0.0, 0.0, 0.0, cos(x), -sin(x), 0.0, 0.0, sin(x), cos(x), 0.0, 0.0, 0.0, 0.0, 1.0])

	@staticmethod
	def Ry(x):
		return Matrix.create([cos(x), 0.0, sin(x), 0.0, 0.0, 1.0, 0.0, 0.0,-sin(x), 0.0, cos(x), 0.0, 0.0, 0.0, 0.0, 1.0])

	@staticmethod
	def Rz(x):
		return Matrix.create([cos(x), -sin(x), 0.0, 0.0, sin(x), cos(x), 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0])

	@staticmethod
	def S(scalar):
		return Matrix.create([scalar, 0.0, 0.0, 0.0, 0.0, scalar, 0.0, 0.0, 0.0, 0.0, scalar, 0.0, 0.0, 0.0, 0.0, 1.0])

	@staticmethod
	def T(x,y,z):
		return Matrix.create([1.0, 0.0, 0.0, x, 0.0, 1.0, 0.0, y, 0.0, 0.0, 1.0, z, 0.0, 0.0, 0.0, 1.0])

	@staticmethod
	def identity():
		return Matrix.create([1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0])

	@staticmethod
	def zeros():
		return Matrix.create([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])


