import numpy as np

rng = np.random.default_rng()
lala =np.arange(9).reshape(3,3)
arr = np.arange(9).reshape(3, 3)
rng.shuffle(arr)
permuted_2d = rng.permutation(arr)
lalash = rng.permutation(lala, axis=1)
fully_random = rng.permutation(arr.flatten()).reshape(3,3)


if __name__ == '__main__':
    print(lala)
    #print(lalash)
   # rng.shuffle(lala)
    #print(lala)
    print(rng.permutation(lala.flatten()).reshape(3,3))
    print(lala)
    for i in arr:
        print(i[0], min(i))
        print(i[-1], max(i))
    print(permuted_2d)
    print(fully_random)
