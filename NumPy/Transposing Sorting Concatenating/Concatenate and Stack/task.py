import numpy as np


a = np.zeros((3, 4), dtype=np.int64)
b = np.arange(0,4,1).reshape(1,4)
c = np.concatenate((a,b),axis=0)

stacked = np.vstack((np.arange(0, 10).reshape(1,10),np.arange(20,30).reshape(1,10),np.arange(40,50).reshape(1,10)))

if __name__ == '__main__':
    print(c)
    print(stacked)
