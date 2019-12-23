# Ruben Navarro
# 12/19/2019
# main.py
# CTCI - Rotate Matrix
# Rotates a NxN Matrix 90 Degrees in place

def rotate90(m):

    layers = len(m) // 2
    length = len(m) - 1

    for layer in range(layers):  # loops through for each layer
        for i in range(layer, length - layer):  # loops through each element
            temp = m[layer][i]  # saves the top element
            # Left -> Top
            m[layer][i] = m[length - i][layer]
            # Bottom -> left
            m[length - i][layer] = m[length - layer][length - i]
            # Right -> bottom
            m[length - layer][length - i] = m[i][length - layer]
            # Top -> Right
            m[i][length - layer] = temp

def displayMatrix(m):
    for row in m:
        print(row)
    print()

matrix = [['A','B','C'], ['D','E','F'], ['G','H','I']]

if len(matrix) == 0:
    print("Error: Matrix is empty")
    exit()

if len(matrix) != len(matrix[0]):
    print("Error: Matrix is not NxN")
    exit()

rotate90(matrix)

displayMatrix(matrix)
