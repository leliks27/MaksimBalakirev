mn = []
for n in range(1000):
    b = bin(n)[2:]
    s = sum(map(int, list(b)))
    if n % 5 == 0:
        b = b[:3] + b
    else:
        b = b + bin(n % 5 * 5)[2:]
    r = int(b,2)
    if r < 313:
        if n % 2 != 0:
            mn.append(n)
print(max(mn))