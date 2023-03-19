'''
A brute force algorithm for computing the convex hull of a set of points on a plane. (i.e. for given a set of points, find the smallest polygon whose vertices are a subset of these points and the remaining points are either inside or on the boundary of this polygon.)
'''
import numpy as np
import matplotlib.pyplot as plt 

N = 20
np.random.seed(1)
#points = np.array([[1,1], [2,3], [4,2], [3,4], [3,3]])
points = 100.0 * np.random.random(size=(N,2)) - 50.0
extreme = np.zeros(points.shape[0])
extreme_points = []
non_extreme_points = []

# for every pair of points, find the straight line connecting the two points, determine if the reminaing points lie on only one side of this line, in wich case, these are "extreme points", i.e. vertices of the convex hull

for i in range(points.shape[0]):
    point1 = points[i] 
    for j in range(points.shape[0] - i - 1):
        point2 = points[i + j + 1]
        #print(f"\npair = {point1}, {point2}")    

        # Equation of line connecting the points: y(x) = y1 + ((y2-y1)/(x2-x1)) * (x-x1)
        #print(f"Equation of line connecting the points: y(x) = {point1[1]} + {(point2[1]-point1[1])/(point2[0]-point1[0]): 0.3f} (x - {point1[0]})")

        m = (point2[1]-point1[1])/(point2[0]-point1[0])
        above = 0
        below = 0

        # check if all the other points lie on one side of the line connecting these two points, if so, these are extreme points, i.e. vertices of the complex-hull polygon
        for k in range(points.shape[0]):
            if((k != i) and (k != i + j + 1)):

                dy = points[k,1] - (point1[1] + m*(points[k,0]- point1[0]))

                if(dy >= 0.0):
                    #print(f"{points[k]} is above the line")
                    above += 1
                else:
                    #print(f"{points[k]} is below the line")
                    below += 1
    
        if(above * below == 0):
            #print("These are extreme points!")
            extreme[i] = 1
            extreme[i+j+1] = 1      
            
for i in range(points.shape[0]):
    if(extreme[i] == 1):
        extreme_points.append(points[i])
    else:
        non_extreme_points.append(points[i])    

#print(f"Extreme points: {extreme_points}")
#print(f"Non-extreme points: {non_extreme_points}")


# make a plot showing the convex-hull
x1, y1 = zip(*extreme_points)
x2, y2 = zip(*non_extreme_points)
plt.figure()
plt.scatter(x1, y1, s = 20, c = 'b')
plt.scatter(x2, y2, s = 20, c = 'r')
plt.show()
