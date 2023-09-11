l = [1, 3, 4, 5, 1, 8, 9, 5, 4, 1, 6, 4, 7]

for i in range(len(l)):
    for j in range(i):
        if l[j] > l[i]:
            l[j], l[i] = l[i], l[j]

print(l)