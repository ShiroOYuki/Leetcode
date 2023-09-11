id = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
computers = [0, 0, 0, 3, 3, 0, 3, 7, 8, 9, 9, 8]

def find(n):
    # 找出 n 的 root
    if computers[n] == n:
        return n
    return find(computers[n])


def union(a, b):
    # 把 a 的 root 連到 b 的 root
    computers[find(3)] = find(2)
    
union(2, 3)
print(computers)
print(find(4))