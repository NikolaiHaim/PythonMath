"""
Functions to make:
Multivariate: Mahalanobis distance


Functions to edit:

Done Functions:
Mean (Mu)
Standard Deviation (Sigma)
Univariate: MLE
Median
Sort
Univariate: Boxplot
Variance
CovarianceMatrix
"""

import MatrixMath

# ------------------------
# Assistance Functions
# ------------------------

def Mean(numbers = None):
    if numbers != None:
        
        count = 0
        sum = 0

        for number in numbers:
            sum += number
            count += 1
        
        return sum/count
    
    else:
        return "Missing data in input"

def StandardDeviation(numbers = None, mode = "population"):
    if numbers == None:
        raise ValueError("Missing data in input")
    
    if mode == "sample":
        return (Variance(numbers, "sample"))**0.5

    else:
        return (Variance(numbers))**0.5
    
def Variance(numbers, mode = "population"):
    if not numbers:
        raise ValueError("Missing data in input")
        
    mu = Mean(numbers)
    sum = 0
    count = 0

    for number in numbers:
        sum += (number - mu)**2
        count += 1
    
    if mode == "sample":
        return (sum/(count-1))

    else:
        return (sum/count)

def Median(numbers = None):
    if numbers != None:
        
        if len(numbers) % 2 == 0:
            return (numbers[int((len(numbers)/2)-1)] + numbers[int(len(numbers)/2)]) / 2
        
        else:
            return (numbers[int((len(numbers)-1)/2)])

    else:
        return "Missing data in input"

def Sort(numbers = None, order = "asc"):
    if order not in ('asc', 'desc'):
        raise ValueError("Order must be either 'asc' or 'desc'")
    
    if numbers != None:
        return sorted(numbers, reverse=(order == 'desc'))
    
    else:
        return "Missing data in input"

def TuplesToLists(data):
    if isinstance(data, tuple):
        return list(data)
    
    elif isinstance(data, list) and all(isinstance(item, tuple) for item in data):
        return [list(item) for item in data]
    
    else:
        raise ValueError("Input must be a single tuple or a list of tuples.")

def CovarianceMatrix(points):
    if not points:
        raise ValueError("Invalid list of points as input.")
 
    if isinstance(points[0], tuple):
        points = [list(point) for point in points]  # Convert tuples to lists

    pointslength = len(points)
    dimensions = len(points[0])

    # Compute vector of averages
    meanvector = [sum(axis) / pointslength for axis in zip(*points)]
    
    # subtract mean vector from all points
    centered_points = [[element[i] - meanvector[i] for i in range(dimensions)] for element in points]

    # Compute covariance matrix
    covariance_matrix = [[
        sum(centered_points[p][i] * centered_points[p][j] for p in range(pointslength)) / (pointslength - 1)
        for j in range(dimensions)]
        for i in range(dimensions)
    ]

    return covariance_matrix

# ------------------------
# Univariate Outlier Detection
# ------------------------

def MLEOutlier(numbers = None):
    if numbers != None:
       
        mu = Mean(numbers)
        sd = StandardDeviation(numbers)
        none_outlier_range = []
        outliers = []
        none_outlier_range.append(mu-(3*sd))
        none_outlier_range.append(mu+(3*sd))

        for number in numbers:
            if number < none_outlier_range[0] or number > none_outlier_range[1]:
                outliers.append(number)
        
        return outliers

    else:
        return "Missing data in input"

def BoxplotOutlier(input = None):
    if input != None:
        
        numbers = Sort(input)

        first_half = numbers[:int(len(numbers)/2)]
        if len(numbers) % 2 == 0:
            last_half = numbers[int(len(numbers)/2):]
        else:
            last_half = numbers[int(len(numbers)/2)+1:]

        Q2 = Median(numbers)
        Q1 = Median(first_half)
        Q3 = Median(last_half)
        IQR = Q3-Q1

        none_outlier_range = []
        outliers = []
        none_outlier_range.append(Q1-(1.5*IQR))
        none_outlier_range.append(Q3+(1.5*IQR))
        
        for number in numbers:
            if number < none_outlier_range[0] or number > none_outlier_range[1]:
                outliers.append(number)

        return outliers

    else:
        return "Missing data in input"

# ------------------------
# Multivariate Outlier Detection
# ------------------------

def MahalanobisDistance(vector):
    if not vector:
        raise ValueError("Invalid list of points as input.") 


# ------------------------
# Testing Area
# ------------------------

data = [28.9, 28.9, 29.0, 29.1, 24.0, 29.2, 29.1, 29.2, 29.4, 29.3, 29.3, 29.4]
data2 = [6.5, 3.8, 3.7, 3.5, 3.4, 3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6]
data3 = [24.0, 28.9, 28.9, 29.0, 29.1, 29.1, 29.2, 29.2, 29.3, 29.4]
data4 = [(5,3),(6,4),(7,5),(5,3),(6,4),(8,6),(7,5),(6,4),(5,3),(20,12)]
data45 = [(1,3),(2,9),(3,3)]

data5 = [(75, 10.5, 45),
        (65, 12.8, 65),
        (22, 7.3, 74),
        (15, 2.1, 76),
        (18, 9.2, 56)]

def test(data):
    print(Mean(data))
    print(StandardDeviation(data))
    print(MLEOutlier(data))
    print(BoxplotOutlier(data))

#test(data)
#print(MahalanobisDistance(data4))
print(MatrixMath.InverseMatrix(CovarianceMatrix(data45)))
print(CovarianceMatrix(data4))