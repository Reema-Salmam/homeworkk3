import numpy as np
import pandas as pa
print(np.__version__)
print(pa.__version__)
array1=np.array([[1,2,3],[4,5,6]])
print(array1)
data=[['reema','21'],['khowla','21']]
df=pa.DataFrame(data,columns=['name','age'])
print(df)

