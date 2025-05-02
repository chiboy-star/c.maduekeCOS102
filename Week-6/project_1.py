
import numpy as np


print("NumPy Version:", np.__version__)


arr = np.array([101, 201, 301, 401, 501])
print(arr)
print(type(arr))


name_list = ['Angel', "Shemi", "Marvel", "Linda"]
age_tuple = (41, 32, 21, 19)
grade_dict = {"CSC102": 89, "MTH 102": 77, "CHM 102": 69, "GST 102": 99}

arr_name_list = np.array(name_list)
arr_age_tuple = np.array(age_tuple)
arr_grade_dict = np.array(list(grade_dict.values()))

print(arr_name_list)
print(arr_age_tuple)
print(arr_grade_dict)


class_num = int(input("How many students are in the CSC 102 class? "))
class_arr = np.array(class_num)

if class_num == 1:
    print("There is only", class_num, "student in CSC 102 class")
else:
    print("There are", class_num, "students in CSC 102 class")


arr_1d = np.array([1, 2, 3, 4, 5])
print(arr_1d)


arr_2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr_2d)


arr_3d = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])
print(arr_3d)


a = np.array(42)
b = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]],
    [[1, 2, 3], [4, 5, 6]]
])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([1, 2, 3, 4, 5])

print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)


arr_high_dim = np.array([1, 2, 3, 4], ndmin=8)
print(arr_high_dim)
print('Number of dimensions:', arr_high_dim.ndim)


arr_access = np.array([1, 2, 3, 4])
print(arr_access[1])
 
arr_2d_access = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('5th element on 2nd row:', arr_2d_access[1, 4])


arr_3d_access = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
print(arr_3d_access[0, 1, 2])


arr_neg = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dim:', arr_neg[1, -1])


arr_slice = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr_slice[1:5])
print(arr_slice[4:])
print(arr_slice[:4])


int_arr = np.array([1, 2, 3, 4])
str_arr = np.array(['apple', 'banana', 'cherry'])
print(int_arr.dtype)
print(str_arr.dtype)


arr_2d_iter = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr_2d_iter:
    for y in x:
        print(y)

arr_3d_iter = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
for x in arr_3d_iter:
    print(x[0][1])
    print(x[1][0])


arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
joined = np.concatenate((arr1, arr2))
print(joined)


arr_split = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr_split, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])
