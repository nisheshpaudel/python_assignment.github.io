def even_num(x):
    enum = []
    for n in x:
        if n % 2 == 0:
            enum.append(n)
    return enum
print(even_num([1, 2, 3, 4, 5, 6, 7, 8, 9]))