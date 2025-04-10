def f(n):
    s = ''
    while n > 0:
        s = str(n % 3) + s
        n = n // 3
    return s

mn = []
for n in range(1000):
    b = f(n)
    s = sum(map(int, list(b)))
    if s % 2 == 0:
        b = '12' + b[2:] + '0'
    else:
        b = '10' + b[2:] + '2'
    r = int(b, 3)
    if r > 105:
        mn.append(n)
print(min(mn))