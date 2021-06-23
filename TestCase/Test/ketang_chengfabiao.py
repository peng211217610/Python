j = 1
for j in range(1,10):
    i = 1
    alist = []
    while i <= j:#当i <= j时，循环添加元素
        alist.append('%s x %s = %2s' % (i, j, i * j))
        i += 1
        continue
    print(str(alist).replace("['","").replace("', '","  ").replace("']",""))