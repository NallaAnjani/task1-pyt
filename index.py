# Data types
# 1.Numeric - int,float,complex,boolean
# 2. sequences-list,Tuple,range,string


# complex numbers:An complex number is represented by “ x + yi “. Python converts the real numbers x and y into complex using the function complex(x,y).
a = 5 + 6j
b = 9 - 4j
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)

# Boolean:Booleans represent one of two values: True or False . Boolean Values. In programming you often need to know if an expression is True or False .
a1=True
print(type(a1))
b1=False
print(type(b1))
print(int(a1))
print(int(b1))
print(5>4)
print(6<=40)

# sequences
# list -collection of hetrogeneous items
# list is mutable
# syntax:[]
l=[1,2,3,4,5,6,77,[3.5,6,86]]
print(l)

# slicing

print(l[2])
print(l[1:5])
print(l[1:9:2])
print(l[:])
print(l[:10])
print(l[0:])
print(l[-3])
print(len(l))
print(l[11][1])
print(l[12][0])
print(l[-4:-8:-1])

# Tuple-collection of hetrogeneous items
# tuple is immutable
# syntax:()

t=(3,34,5,7,7,9,2,234,77,90,(4,6,7,9))
#slicing
print(l[2])
print(l[1:5])
print(l[1:9:2])
print(l[:])
print(l[:10])
print(l[0:])
print(l[-3])
print(len(l))
 
# Range- range of items
print(list(range(0,100)))
print(list(range(50,30,-2)))
print(list(range(100,0,-2)))




