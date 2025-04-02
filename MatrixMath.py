"""
Commented functions / Functions in need of update:

Functions to make:
IsInvertible
Eigenvalue 
Eigenvector
IsLinearlyIndependent
"""

# ------------------------
# PRIMARY FUNCTIONS
# ------------------------

# Checks if the matrix is upper triangular
def IsUpperTriangular(matrix):
    if not IsSquare(matrix):
        return False
    
    size = len(matrix)
    
    for i in range(1, size):
        for j in range(0, i):
            if matrix[i][j] != 0:
                return False
            
    return True

# Checks if the matrix is lower triangular
def IsLowerTriangular(matrix):
    if not IsSquare(matrix):
        return False
    
    size = len(matrix)

    for i in range(size):
        for j in range(i+1, size):
            if matrix[i][j] != 0:
                return False
            
    return True

# Checks if the matrix is diagonal
def IsDiagonal(matrix):
    if not IsSquare(matrix):
        return False
    
    size = len(matrix)
    
    for i in range(size):
        for j in range(size):
            if i != j and matrix[i][j] != 0:
                return False
    
    return True

# Calculates the determinant of an NxN matrix
def DeterminantOfMatrix(matrix = None):
    
    # Checks if matrix is square as it needs to be square to have a determinant
    if IsSquare(matrix):

        size = len(matrix)

        # shortcut: if matrix is diagonal, upper triangular, or lower triangular
        if IsDiagonal(matrix) or IsUpperTriangular(matrix) or IsLowerTriangular(matrix):
            
            determinant = 1

            for i in range(size):
                determinant *= matrix[i][i]
            
            return determinant
        
        else:

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

# Returns the transposed matrix of an NxM matrix
def TransposeMatrix(matrix = None):
    if not checkForMatrix(matrix):
        raise ValueError("Invalid matrix input.")   
        
    rows, cols = shape(matrix)
    tmat = [[0] * rows for _ in range(cols)]   

    for i in range(rows):
        for j in range(cols):
            tmat[j][i] = matrix[i][j]

    return tmat

# Returns the adjugate matrix of an NxN matrix
def AdjugateMatrix(matrix):
    if not IsSquare(matrix):
        raise ValueError("Adjugate is only defined for square matrices.")

    size = len(matrix)
    
    # Compute cofactor matrix
    cofactor_matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            # Get the minor matrix (exclude row i and column j)
            minor = [row[:j] + row[j+1:] for row in (matrix[:i] + matrix[i+1:])]
            
            # Compute the determinant of the minor matrix
            cofactor_matrix[i][j] = ((-1) ** (i + j)) * DeterminantOfMatrix(minor)

    # Transpose the cofactor matrix to get the adjugate
    return TransposeMatrix(cofactor_matrix)

# Returns the NxM matrix given, multiplied by a scalar
def ScalarMultiplication(matrix, scalar):
    if not checkForMatrix:
        raise ValueError("Missing matrix as input")
    
    rows, cols = shape(matrix)

    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = matrix[i][j]*scalar
    
    return matrix

# Returns the inverese matrix of an NxN matrix
def InverseMatrix(matrix):
    if not IsSquare(matrix):
        raise ValueError("Inverse matrix is only defined for square matrices.")
    
    det = DeterminantOfMatrix(matrix)

    if det == 0:
        raise ValueError("Inverse matrix is only defined for matrices with non-zero determinants.")
    
    scalar = 1 / det
    adj = AdjugateMatrix(matrix)

    return ScalarMultiplication(adj,scalar)

# Returns the product of any given MxN, NxP matrices
def MatrixMultiplication2(matrix1, matrix2):
    
    rows1, cols1 = shape(matrix1)
    rows2, cols2 = shape(matrix2)

    if cols1 != rows2:
        raise ValueError("For matrix multiplication, the number of columns in the first "
        "matrix must be equal to the number of rows in the second matrix.")

    # Create a result matrix filled with zeros
    mmat = [[0] * cols2 for _ in range(rows1)]

    # Perform matrix multiplication
    for i in range(rows1):  
        for j in range(cols2):  

            sum_value = 0  

            for k in range(cols1):  

                sum_value += matrix1[i][k] * matrix2[k][j]

            mmat[i][j] = sum_value  

    return mmat

# ------------------------
# ASSISTANCE FUNCTIONS
# (non calculatory functions)
# ------------------------

# Returns true if there is a matrix
def checkForMatrix(matrix = None):
    if matrix == None:
        print("ERROR: Missing matrix as input")
        exit(0)

    elif type(matrix) != list:
        print("ERROR: Invalid matrix as input")
        exit(0)

    else:
        return True

# Returns the shape of the matrix as a tuple (rows, cols)
def shape(matrix = None):
    if not checkForMatrix(matrix):  # Ensure the input is valid
        return None
    
    if not matrix:  # Check for empty matrix
        return 0, 0
    
    if isinstance(matrix[0], list):  # Check if it's a 2D matrix
        return len(matrix), len(matrix[0])
    
    return len(matrix), 1  # It's a vector (1D list)
    
# Checks if the matrix is square
def IsSquare(matrix = None):
    if checkForMatrix(matrix) == True:
        
        # Checks if there are as many rows as there are columns
        if shape(matrix)[0] == shape(matrix)[1]:
            return True
        
        else:
            return False

# Given a matrix and a column number, returns the whole column as a list       
def columnStripper(matrix, column):
    if not checkForMatrix(matrix):
        raise ValueError("No matrix was given")
    
    if not column:
        raise ValueError("No column was given")
    
    col = [row[column-1] for row in matrix]

    return col
