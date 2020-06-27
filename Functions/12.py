def compute(n):
 return lambda x : x * n
product = compute(2)
print("Two times the number 55 =", product(55))
product = compute(5)
print("Five times the number of 55 =", product(55))
