import Rhino.Geometry as rg

pointA = rg.Point3d(-10, 9, 0)
pointB = rg.Point3d(-15, 5, 0)

vect = pointA - pointB
print (type(vect))

