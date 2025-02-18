"""
Commented functions / Functions in need of update:
IsDiagonal

Functions to make:
IsInvertible
Eigenvalue 
Eigenvector
IsLinearlyIndependent
TransposeMatrix
"""


# Checks if the matrix is square
def IsSquare(matrix = None):
    if checkForMatrix(matrix) == True:
        
        # Checks if there are as many rows as there are columns
        if shape(matrix)[0] == shape(matrix)[1]:
            return True
        
        else:
            return False


# Checks if the matrix is upper triangular
def IsUpperTriangular(matrix = None):
    if IsSquare(matrix) == True:
        indices = []
        
        for x in matrix: 
            for y in x:
                if matrix.index(x) > x.index(y):
                   indices.append((matrix.index(x), x.index(y)))

        for x in indices:
            if matrix[x[0]][x[1]] != 0:
                return False
            
            else:
                return True
    
    else:
        return False


# Checks if the matrix is lower triangular
def IsLowerTriangular(matrix = None):
    if IsSquare(matrix) == True:
        indices = []

        for x in matrix: 
            for y in x:
                
                if matrix.index(x) < x.index(y):
                   indices.append((matrix.index(x), x.index(y)))

        for x in indices:
            
            if matrix[x[0]][x[1]] != 0:
                return False
            
            else:
                return True
    
    else:
        return False


# Checks if the matrix is diagonal
def IsDiagonal(matrix = None):
    if IsSquare(matrix) == True:
        
        if IsLowerTriangular(matrix) == True and IsUpperTriangular(matrix) == True:
            return True
        
        else:
            return False
    
    # [NONE SQUARE MATRIX CAN BE DIAGONAL]
    else:
        return False


# Calculates the determinant of an NxN matrix
def DeterminantOfMatrix(matrix = None):
    size = len(matrix)
    # shortcut: if matrix is diagonal, upper triangular, or lower triangular
    if IsDiagonal(matrix) or IsUpperTriangular(matrix) or IsLowerTriangular(matrix):
        
        determinant = 1
        
        for diagonalelement in range(size):
            # Multiply diagonal elements
            determinant *= matrix[diagonalelement][diagonalelement]  
        return determinant

    # Checks if matrix is square as it needs to be square to have a determinant
    elif IsSquare(matrix) == True:
        
        size = len(matrix)
        determinant = 0
        
        # Base case: If the matrix is 1x1, return the only element
        if size == 1:
            return matrix[0][0]

        # Base case: If the matrix is 2x2, use the direct determinant formula
        if size == 2:
            return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        
        # Recursive case: Expand along the first row (row 0)
        for column in range(size):
            # Construct the minor matrix directly (removing row 0 and column 'col')
            submatrix = [row[:column] + row[column + 1:] for row in matrix[1:]] 

            # Compute the determinant recursively with the cofactor sign
            cofactor = (-1) ** column * matrix[0][column] * DeterminantOfMatrix(submatrix)
            determinant += cofactor

        return determinant

    else: 
        print("Matrix has no determinant as it isn't square")
        return False


"""
ASSISTANCE FUNCTIONS
(non calculatory functions)
"""

def checkForMatrix(matrix = None):
    if matrix == None:
        print("ERROR: Missing matrix as input")
        exit(0)
    elif type(matrix) != list:
        print("ERROR: Invalid matrix as input")
        exit(0)
    else:
        return True


def shape(matrix = None):
    if checkForMatrix(matrix) == True:
        return len(matrix[0]), len(matrix)
    else:
        return None