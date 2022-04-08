import matplotlib.pyplot as plt
import numpy as np

# eng = matlab.engine.start_matlab()

filename = input("Enter filepath of txt file: ")

a = open(filename, "r")
lines = a.readlines()
degrees = list()
distance = list()
distanceNonAdc= list()
for x in lines:
    distance.append(int(x.split(' ')[2]))
    distanceNonAdc.append(float(x.split(' ')[1]))
    degrees.append(int(x.split(' ')[0]))
a.close()

#print(degrees)
#print(distance)


thetadegrees= list()
for i in range(len(degrees)):
    theta = int(degrees[i]) * (np.pi / 180)
    thetadegrees.append(theta)


#print(thetadegrees)

i = 1
while i < len(thetadegrees):
    thetadegrees.insert(i, 0)
    i += 2
i = 1
while i < len(distance):
    distance.insert(i, 0)
    i += 2
i = 1
while i < len(distanceNonAdc):
    distanceNonAdc.insert(i, 0)
    i += 2


#print(distanceNonAdc)
# print(distance)
ax = plt.subplot(111, projection='polar')
ax.plot(thetadegrees, distanceNonAdc)
#a= plt.subplot(1,1,1, projection='polar')
#a.plot(thetadegrees,distance)
plt.show()

# x= [1,2,3]
# y= [1,4,9]

# plt.plot(x,y)
# plt.show()