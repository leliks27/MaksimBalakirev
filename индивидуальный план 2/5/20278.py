mn = []
for n in range(1000):
    b = bin(n)[2:]
    s = sum(map(int, list(b)))
    if s % 2 == 0:
        b = '101' + b[3:] + '01'
    else:
        b = '111' + b[3:] + '10'
    r = int(b,2)
    if r < 385:
        mn.append(n)
print(max(mn))