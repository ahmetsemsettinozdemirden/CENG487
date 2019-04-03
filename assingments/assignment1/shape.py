# CENG 487 Assignment1 by
# Ahmet Semsettin Ozdemirden
# StudentNo: 230201043
# Date: 03-2019

class Shape:

    def __init__(self, pos, vertices, matrixStack):
        self.pos = pos
        self.vertices = vertices
        self.matrixStack = matrixStack

    def applyMatrixToVertices(self, mat3d):
        for i, vertex in enumerate(self.vertices):
            self.vertices[i] = mat3d.multiply(vertex)

    def applyMatrixStack(self):
        for matrix in self.matrixStack:
            self.applyMatrixToVertices(matrix)
            