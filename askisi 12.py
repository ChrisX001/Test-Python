op = open("k.txt","r")
a = op.read()
q = len(a)
    while q > 0:
        k = op.read(q)
        t = ord("k")
        y = 255 - t
        z = chr(y)
        print (z)
        q = q - 1
op.close