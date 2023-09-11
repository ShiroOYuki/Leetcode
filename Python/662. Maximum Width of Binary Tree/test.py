a = [1, 2, 3, None, 4, 5, None, 6, 7, 8, None, 9]
print(list(filter(lambda i: i != None, a)))
a = 0
print(0 if 0 == None else 1)