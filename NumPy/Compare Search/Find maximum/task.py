import numpy as np

data = np.genfromtxt('data.csv', dtype= np.int64, delimiter=',')
maxima = np.expand_dims(np.argmax(data, axis=1),1)
result = np.take_along_axis(data, maxima, axis=1)

if __name__ == '__main__':
    print(data)
    print(maxima)
    print(result)
