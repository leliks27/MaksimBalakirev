def f(n):
    s = ''
    while n > 0:
        s = str(n % 4) + s
        n = n // 4
    return s

mn = []
for n in range(1000):
    b = f(n)
    if n % 4 == 0:
        b = '2' + b + '03'
    else:
        b = b + f(n % 4 * 5)
    r = int(b, 4)
    if r < 567:
        mn.append(n)
print(max(mn))