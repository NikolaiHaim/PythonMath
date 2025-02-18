import MatrixMath

matrix0 = [[1]]

matrix1 = [[1,2],
           [3,4]]

matrix2 = [[1,2,3],
           [4,5,6],
           [7,8,9]]

matrix3 = [[1,2,3,4],
           [5,6,7,8],
           [9,10,11,12],
           [13,14,15,16]]

matrix4 = [[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,18,19,20],
           [21,22,23,24,25]]

matrix5 = [[1,2],
           [3,4],
           [5,6]]

matrix6 = [[1,2,3],
           [4,5,6]]

matrix7 = [[1,0,0,0],
           [5,6,0,0],
           [9,10,11,0],
           [13,14,15,16]]

matrix8 = [[1,2,3,4],
           [0,6,7,8],
           [0,0,11,12],
           [0,0,0,16]]

matrix9 = [[1,0,0,0],
           [0,6,0,0],
           [0,0,11,0],
           [0,0,0,16]]

listofmatrices = []

listofmatrices.append(matrix0)
listofmatrices.append(matrix1)
listofmatrices.append(matrix2)
listofmatrices.append(matrix3)
listofmatrices.append(matrix4)
listofmatrices.append(matrix5)
listofmatrices.append(matrix6)
listofmatrices.append(matrix7)
listofmatrices.append(matrix8)
listofmatrices.append(matrix9)


for x in listofmatrices:
    #print("Matrix " + str(listofmatrices.index(x)+1) + ": " + str(MatrixMath.IsSquare(x)))
    #print("Matrix " + str(listofmatrices.index(x)+1) + ": " + str(MatrixMath.IsUpperTriangular(x)))
    #print("Matrix " + str(listofmatrices.index(x)+1) + ": " + str(MatrixMath.IsLowerTriangular(x)))
    #print("Matrix " + str(listofmatrices.index(x)+1) + ": " + str(MatrixMath.IsDiagonal(x))) 
    #print("Matrix " + str(listofmatrices.index(x)+1) + ": " + str(AssistanceFunctions.shape(x)))
    if MatrixMath.IsSquare(x):
        print("Matrix " + str(listofmatrices.index(x)) + " Determinant: " + str(MatrixMath.DeterminantOfMatrix(x)))
    print("")
    #print(AssistanceFunctions.shape(x))

#MatrixMath.DeterminantOfMatrix(matrix6)

#print(MatrixMath.IsSquare(matrix9))
#print(MatrixMath.IsLowerTriangular(matrix9))
#print(MatrixMath.IsUpperTriangular(matrix9))
#print(MatrixMath.IsDiagonal(matrix9))
# print(matrix1[0].index(2))

