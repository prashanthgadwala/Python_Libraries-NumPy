import numpy as np


def reshape_transpose(start, stop, step=1):
    a= np.arange(start,stop,step)
    a= a.reshape(1,a.shape[0])
    print(a)
    return a.transpose()


if __name__ == '__main__':
    print(reshape_transpose(1, 100, 10))
    print(reshape_transpose(0, 5))
