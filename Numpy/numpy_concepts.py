import numpy as np
# numpy is faster than lists because it stores the data in fixed type. It stores values in Int32 and Int16 List
# consists of size, reference count, object type, object value which is approximately 8 bytes. Consumes more memory.
# Numpy utilizes contiguous memory.
# Benefits: SIMD Vector Processing, Effective Cache Utilization.
# Applications of Numpy: Mathematics(MATLAB replacement), Backend, Plotting, Store Images, Machine Learning etc.

# Initialize array
a =np.array([1,2,3])
print(a)
b = np.array([[9.0,8.0,7.0],[6,4.5,3.5]],dtype='int16')
print(b)

# Get Dimension
print(a.ndim)

# Get Shape
print(b.shape)

# Get type
print(a.dtype)

# Get size in Bytes
print(a.itemsize)
print(b.itemsize)

# Get Total Size
print(a.nbytes)
print(b.nbytes)
c = np.array([[1,2,3,4,5,6,7],[11,12,34,56,78,65,34]])

# Get shape
print(c.shape)

# Fetch a specific element
print(c[1, 5])

# Indexing starts from 0.

# Get a specific row

print(c[0, :])

# Get a specific column

print(c[:, 0])

# Colon specifies indexing till the last element(inclusive)

# Get using  [startindex:endindex:steps]. It is  exclusive.

print(c[0, 1:6:2])

# Changing array values
c[1,5] =20
print(c)

c[:, 2] = [1,2]
print(c)

# 3-D example
d = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(d)

# To get a specific element (work outside in)

# Initialise all 0s matrix

print(np.zeros((2,3)))

# All one's matrix

print(np.ones((4,3,3)))

# Any other matrix

print(np.full((2,2),99))

# Any other number (full_like)

print(np.full_like(c.shape,33))

# Random Decimal Numbers

print(np.random.rand(4,3))

# Random Decimal using previous structures.

print(np.random.random_sample(a.shape))

# Random Integer values

print(np.random.randint(7,size=(3,3)))

print(np.random.randint(4,7,size=(3,3)))

# Identity matrix

print(np.identity(5))

# Repeating arrays
arr = np.array([[1,2,3]])
r1 = np.repeat(arr,3,axis=0)
print(r1)

# Printing the required array

e = np.ones((5, 5))
e[1:4, 1:4]= 0
e[2, 2] = 9
print(e)

# Be careful when copying arrays
a = np.array([1,2,3])
b =a
b[0]= 100
print(b)
print(a)

# Now both a and b points to the same value, therefore if we change b, a will also get changed.
# To prevent this we can use the copy function

a = np.array([1,2,3])
b =a.copy()
b[0]= 100
print(b)
print(a)

# MATHEMATICS USING NUMPY

# Basic calculations

a = np.array([1,2,3,4,5])
print(a+2)
print(a-2)
print(a*2)
print(a/2)
b = np.array([-1,-2,-3,-4,-5])
print(a+b)
print(a**2)

# Sine and Cosine
print(np.sin(a))
print(np.cos(a))

# Linear Algebra
a = np.ones((2,3))
print(a)
b =np.full((3,2),2)
print(b)

# For matrix multiplication of two matrices rows of first matrix should be equal to columns of second matrix
print(np.matmul(a,b))

c = np.identity(3)
c = np.linalg.det(c)
print(c)

# Statistics

stats = np.array([[1,2,3],[4,5,6]])
minimum = np.min(stats)
maximum = np.max(stats)
print(minimum,maximum)

# We can use axis with min and max function

# Reorganizing arrays
before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)

after = before.reshape((4,2))
print(after)


# Vertically stacking arrays
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
v = np.vstack([v1,v2])
print(v)

# Horizontal Stacking
h1 = np.ones((2,4))
h2 = np.zeros((2,2))
h = np.hstack([h1,h2])
print(h)

# Advanced Indexing and Boolean Masking
a = np.array([[2,33,45,54],[23,34,435,5]])
print(a>22)

# Indexing using list
a = np.array([1,2,3,4,5,6,7,7,8,87])
print(a[[0,1,4]])
