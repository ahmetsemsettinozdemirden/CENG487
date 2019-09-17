# CENG 487 Assignment4 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 05-2019
from vector import *
from matrix import *

class BoundingBox:
	def __init__(self):
		self.min = Point3f(1000, 1000, 1000)
		self.max = Point3f(-1000, -1000, -1000)

	def volume(self):
		diagonal = self.max - self.min
		return sqrlen(diagonal)

	def center(self):
		return 0.5 * (self.min + self.max)

	def expand(self, point):
		if (point.x < self.min.x): self.min.x = point.x
		if (point.y < self.min.y): self.min.y = point.y
		if (point.z < self.min.z): self.min.z = point.z
		if (point.x > self.max.x): self.max.x = point.x
		if (point.y > self.max.y): self.max.y = point.y
		if (point.z > self.max.z): self.max.z = point.z

	def union(self, other):
		if (other.min.x < self.min.x): self.min.x = other.min.x
		if (other.min.y < self.min.y): self.min.y = other.min.y
		if (other.min.z < self.min.z): self.min.z = other.min.z
		if (other.max.x > self.max.x): self.max.x = other.max.x
		if (other.max.y > self.max.y): self.max.y = other.max.y
		if (other.max.z > self.max.z): self.max.z = other.max.z

	def contains(self, point):
		return 	self.min.x < point.x and point.x < self.max.x and \
				self.min.y < point.y and point.y < self.max.y and \
				self.min.z < point.z and point.z < self.max.z

	def encloses(self, other):
		return 	other.min.x >= self.min.x and other.min.y >= self.min.y and other.min.z >= self.min.z and \
				other.max.x <= self.max.x and other.max.y <= self.max.y and other.max.z <= self.max.z

	def overlaps(self, other):
		return	not (	self.max.x <= other.min.x or other.max.x <= self.min.x or \
						self.max.y <= other.min.y or other.max.y <= self.min.y or \
						self.max.z <= other.min.z or other.max.z <= self.min.z )
