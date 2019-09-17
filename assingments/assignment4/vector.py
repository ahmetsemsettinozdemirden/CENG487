# CENG 487 Assignment4 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 05-2019
from math import pi,sin,cos,sqrt,acos

__all__ = ['HCoord', 'Vector3f', 'Point3f', 'ColorRGBA']

class HCoord:
	def __init__(self, x, y, z, w):
		self.x = x
		self.y = y
		self.z = z
		self.w = w

	def sqrlen(self):
		return 1.0 * self.x * self.x + self.y * self.y + self.z * self.z + self.w * self.w

	def len(self):
		return sqrt( self.sqrlen() )

	def dot(self,other):
		return 1.0 * other.x * self.x + other.y * self.y + other.z * self.z + other.w * self.w

	def cross(self,other):
		return HCoord(	self.y * other.z - self.z * other.y, \
						self.z * other.x - self.x * other.z, \
						self.x * other.y - self.y * other.x, \
						self.w)

	def cosa(self, other):
		return min( max( self.dot(other) / (self.len() * other.len() ), 0.0), 1.0 )

	def angle(self, other):
		return acos(self.cosa(other))

	def normalize(self):
		l = self.len()
		return HCoord(self.x / l, self.y / l, self.z / l, self.w / l)

	def project(self, other):
		return other.unit() * (self.len() * self.cosa(other))

	def Rx(self,x):
		m = Matrix.create([1,0,0,0,0,cos(x),-sin(x),0,0,sin(x),cos(x),0,0,0,0,1])
		return m.vecmul(self)

	def Ry(self, x):
		m = Matrix.create([cos(x), 0, sin(x), 0, 0, 1, 0,0, -sin(x), 0, cos(x), 0, 0, 0, 0, 1])
		return m.vecmul(self)

	def Rz(self, x):
		m = Matrix.create([cos(x), -sin(x), 0, 0, sin(x), cos(x), 0, 0, 0, 0, 1, 0, 0, 0, 0, 1])
		return m.vecmul(self)

	def S(self,scalar):
		return self * scalar

	def T(self,x,y,z):
		m = Matrix.create([1, 0, 0, x, 0, 1, 0, y, 0, 0, 1, z, 0, 0, 0, 1])
		return m.vecmul(self)

	def __add__(self, other):
		x = 1.0 * self.x + other.x
		y = 1.0 * self.y + other.y
		z = 1.0 * self.z + other.z
		w = 1.0 * self.w + other.w
		return HCoord(x, y, z, w)

	def __sub__(self, other):
		return self + (-1 * other)

	def __div__(self, scalar):
		if (scalar == 0):
			return self
		else:
			return HCoord(self.x / scalar, self.y / scalar, self.z / scalar, self.w / scalar)

	def __mul__(self, scalar):
		return HCoord(scalar * self.x, scalar * self.y, scalar * self.z, self.w*scalar)

	def __rmul__(self, scalar):
		return HCoord(scalar * self.x, scalar * self.y, scalar * self.z, self.w*scalar)

	def __str__(self):
		return "(" + str(self.x) + " " + str(self.y) + " " + str(self.z) + " " + str(self.w) +")"

	def __repr__(self):
		return self.__str__()

class Vector3f(HCoord):
	def __init__(self,x,y,z):
		HCoord.__init__(self, x, y, z, 0)

class Point3f(HCoord):
	def __init__(self, x, y, z):
		HCoord.__init__(self, x, y, z, 1.0)

	def __sub__(self, other):
		return Vector3f( 	self.x - other.x, \
							self.y - other.y, \
							self.z - other.z )

	def __add__(self, other):
		return Point3f( 	self.x + other.x, \
							self.y + other.y, \
							self.z + other.z )

	def __mul__(self, scalar):
		return Point3f(scalar * self.x, scalar * self.y, scalar * self.z)

class ColorRGBA(HCoord):
	def __init__(self, r, g, b, a):
		HCoord.__init__(self, r, g, b, a)
		self.r = self.x
		self.g = self.y
		self.b = self.z
		self.a = self.w
