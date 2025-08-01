import numpy as np

# arr = np.array([2,5,6,8,3])
# print(type(arr))
# print(arr[1])

# arr0 = np.array(3)
# print(arr0.ndim)
# np.array([3,6,7,9,1,2])
# print(arr1.ndim)

# print(arr1[3])
# print(arr1[0:3])
# print(arr1[2:])
# print(arr1[:4])
# print(arr1[:])
# print(arr1[::2)



# arr2 = np.array([
#     [2,4,7],
#     [1,7,9],
#     [7,8,1]
# ])
# print(arr2.ndim)

# arr3 = np.array([
#     [
#         [1,3,6],
#         [4,8,9]
#     ]
# ])
# print(arr3.ndim)

# arr2 = np.array([
#     [3,5,7,6],
#     [1,9,4,3]
# ])
# print(arr2.shape)
# print(arr2[0:2,0:3])
# arr = np.array([1, 2, 3, 4, 5])
# x = arr.view()
# x[0] = 42
#
# print(arr)
# print(x)arr = np.array([1, 2, 3, 4, 5])
# x = arr.copy()
# arr[0] = 42
#
# print(arr)
# print(x)r

# arr = np.array([1, 2, 3])
# for i in arr:
#     print(i)

# arr = np.array([
#     [1, 2, 3],
#     [4, 5, 6]
# ])
# for i in arr:
#     for j in i:
#         print(j)

# arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
#
# for i in arr:
#     for j in i:
#         for k in j:
#             print(k)

# for x in np.nditer(arr):
#   print(x)

# arr = np.array([1, 2, 3])
#
# for i in np.nditer(arr):
#     print(i)

# arr = np.array([10, 24, 13])
#
# for idx,value in np.ndenumerate(arr):
#     print(idx,value)


# arr1 = np.array([1, 2, 3])
#
# arr2 = np.array([4, 5, 6])
#
# # arr = np.concatenate((arr1, arr2))
# #
# # print(arr)
# arr = np.stack((arr1, arr2), axis=1)
# print(arr)

#
# arr = np.array([1, 7,2, 3, 4, 5, 6])
#
# newarr = np.array_split(arr, 3)
# print(newarr)


#arr = np.array([1, 2, 3, 4, 5, 4, 4])
#
# x = np.where(arr%2 == 0)
#
# print(x)
#
#x = np.searchsorted(arr, 2)
#
#print(x)

#arr = np.array([6, 7, 8, 9])

#x = np.searchsorted(arr, 7, side='left')

#print(x)


/