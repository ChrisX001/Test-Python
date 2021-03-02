op = open("x.txt","r")
def team (p1,p2) :
    t = 0
    e = 0
    while t < len(p2) :
        c = False
        while c = False && e < len(p2) :
            if t != e && (p2[e] + p2[t] == 20):
                print p1[e]
                print p1[f]
                p1.pop(e)
                p1.pop(t)
                p2.pop(e)
                p2.pop(t)
                t = t - 1
            else :
                e = e + 1
            t = t + 1
read = op.readline()
x = 0
u = []
su = []
while read != "":
    l.spli("")
    for i in range (0,len(l)) :
        u.append(l[i].strip())
        su.appent(len(l[i]))
        x = x + 1
for i in range (0,x) :
    print u[i]
    print su[i]
team (u,su)
op.close