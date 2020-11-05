import random, math
iterations = 1024*1024*1024

points_in_circle = 0
radius = 1.0


for i in range(iterations):
    x = random.random()
    y = random.random()
    if math.sqrt(x*x + y*y) < radius:
        points_in_circle = points_in_circle + 1

pi = (points_in_circle/iterations)*4.0
print("The value of PI is ", pi)
print("The actual value of PI is ", math.pi)
print("The error is ", abs(pi-math.pi))