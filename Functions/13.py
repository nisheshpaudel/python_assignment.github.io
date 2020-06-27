week_days = [('Saturday', 7), ('Tuesday', 3), ('Thursday', 5), ('Monday', 2), ('Friday', 6), ('Sunday', 1), ('Wednesday', 4)]
print("Original list of days in a tuples:")
print(week_days)
week_days.sort(key = lambda x: x[1])
print("\nSorting the week days in a tuple:")
print(week_days)