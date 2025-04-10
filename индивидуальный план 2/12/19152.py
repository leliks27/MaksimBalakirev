for n in range (3, 10000):
    s = '59' + '8' * n
    while '68' in s or '988' in s or '888' in s:
        s = s.replace('68', '8', 1)
        s = s.replace('988', '86', 1)
        s = s.replace('888', '9', 1)
    p = 1
    s = sum(map(int, s))
    print(s, n)
# 27 7
# 3 в кубе равно 27, соответственно ответ 7
