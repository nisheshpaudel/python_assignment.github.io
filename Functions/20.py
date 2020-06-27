array_nums1 = [-9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 5, 7, 8, 9]
array_nums2 = [-1, -3, -4, -6, -7, -9, 0, 2, 4, 5, 8, 9]
print("Original arrays:")
print(array_nums1)
print(array_nums2)
inter = list(filter(lambda x: x in array_nums1, array_nums2))
print ("\nIntersection of the two arrays: ",inter)