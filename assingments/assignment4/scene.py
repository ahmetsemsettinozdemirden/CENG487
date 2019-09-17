# CENG 487 Assignment4 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 05-2019
from shapes import Shape

class Scene:
	def __init__(self):
		self.originalNodes = []
		self.nodes = []

	def add(self, node):
		self.originalNodes.append(node)
		self.nodes.append(node)

  # helper method for subdivision (subdivision could be implemented more efficiently)
	def subdivide(self, subdivisionLevel):
		nodes = []
		for originalNode in self.originalNodes:
			node = Shape(originalNode.name)
			# start from level 2 since level 1 subdivision is equal to object itself.
			for i in range(subdivisionLevel - 1):
				node.subdivide()
			nodes.append(node)
		self.nodes = nodes
