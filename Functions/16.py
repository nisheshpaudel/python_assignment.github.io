nums = [-1, -3, -4, -6, -7, -9, 0, 2, 4, 5, 8, 9]
print("Original list of integers:")
print(nums)
print("\nSquare every number in the list:")
square_nums = list(map(lambda x: x ** 2, nums))
print(square_nums)
print("\nCube every number in the list:")
cube_nums = list(map(lambda x: x ** 3, nums))
print(cube_nums)