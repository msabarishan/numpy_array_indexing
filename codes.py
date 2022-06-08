import numpy as np
# Create 3x3 numpy
Z = np.arange(9).reshape(3,3)
# Indexing elements from different location
a=Z[-1,-1]
b=Z[0]
c=Z[1:,1:]
d=Z[::2,::2]
e=Z[[0,1],[0,2]]
print(a,"\n\n",b,"\n\n",c,"\n\n",d,"\n\n",e)
