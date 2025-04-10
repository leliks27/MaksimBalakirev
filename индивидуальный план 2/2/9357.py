print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x <= y) == (w and (not z)) #(x <= y) or ((not w) == z)
                if f == 1:
                    print(x, y, z, w)
#