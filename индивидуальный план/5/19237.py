def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s

mn = []
for n in range(1, 1000):
    b = f(n)
    summa = sum(map(int, list(b)))
    if n % 3 == 0:
        b = b + b[-2:]
    else:
        b = b + f(summa)
    r = int(b, 3)
    if r > 220 and r % 2 == 0:
        mn.append(r)
print(min(mn))