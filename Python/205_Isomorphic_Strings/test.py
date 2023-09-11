def test():
    a = 1
    b = 2
    c = 3
    d = 4
    r1 = (a, b)
    r2 = (c, d)
    return r1, r2

(a, b), (c, d) = test()
print(test())