
for n in range (4, 10000):
    s = '2' + '7' * n
    while '27' in s or '777' in s or '377' in s:
        s = s.replace('27', '7', 1)
        s = s.replace('777', '3', 1)
        s = s.replace('377', '72', 1)
    p = 1
    for j in s:
        p = p * int(j)
    if p % 3 == 0 and str(p)[-1] == '1':
        print(n)
#9996