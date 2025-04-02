"""
Functions to make:
Agglomerative
Single Linkage
CompleteLinkage
AverageLinkage

Functions to edit:

Done Functions:
DistanceFunc
DistanceMatrix
"""

import MatrixMath

points = [(2,3),(5,7),(1,8),(10,12),(14,14),(15,17),(2,3),(15,17)]

def DistanceFunc(p1, p2, distance = 1):
    if p1 != None and p2 != None:
        return (abs(p1[0]-p2[0])**distance + abs(p1[1]-p2[1])**distance)**(1/distance)   
    
    else:
        print("Invalid points as input")
        return False

def DistanceMatrix(points=None, distmethod=1):
    if points is not None:
        distmat = []
        for i in range(len(points)):
            distmat.append([None] * len(points))
        
        for i in range(len(points)):
            for j in range(len(points)):
                distmat[i][j] = DistanceFunc(points[i], points[j], distmethod)

        for row in distmat:
            print(row)

        return distmat
    else:
        print("Invalid points as input")
        return False

#print(ManhattanDistance(points[0],points[1]))
#d = DistanceMatrix(points, 1)
#print(MatrixMath.shape(d))
#print(MatrixMath.shape(DistanceMatrix(points)))

points2 = [(8.5,8.5), (0,0)]
#print(DistanceFunc(points2[0],points2[1],2))

points3 = [(1,2),(1,4),(3,2),(3,4),(4,1),(4,2),(5,1)]
DistanceMatrix(points3, 2)