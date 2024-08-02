def u(n):
    c = []
    d = []
    for a in range(1,20):
        for b in range (1,20):
            if n % (a + b) == 0 and a != b and a < b:
                c.append(str(a)+str(b))
                d = ''.join(map(str, c))
    return d
    
result = u(20)
print(result)
