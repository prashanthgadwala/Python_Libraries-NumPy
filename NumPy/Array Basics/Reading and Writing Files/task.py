import numpy as np

data = 'somedata.csv'
arr = np.genfromtxt('somedata.csv', delimiter=',', skip_header=3)

if __name__ == '__main__':
    arr = np.genfromtxt('somedata.csv', delimiter=',', skip_header=1)
    print(arr)
    print(arr.shape)
    print(arr.dtype)
    np.savetxt('test.out', arr[:10], delimiter=',')  # Saves the first 10 lines to a new file
