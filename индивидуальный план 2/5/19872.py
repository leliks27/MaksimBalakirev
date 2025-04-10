def f(n):
    s = ''
    while n > 0:
        s = str(n % 7) + s
        n = n // 7
    return s

mn = []
for n in range(1001):
    b = f(n)
    if n % 2 == 0:
        b = '52' + b + '1'
    else:
        b = b[-1] + b[1:-1] + b[0] + '15'
    b = b.lstrip('0')
    r = str(int(b, 7))
    if len(b) == 4:
        mn.append(n)
print(max(mn))