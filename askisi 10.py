f = open("r.txt", "r")
c = f.read()
g = len(c)
r = 0
op = {
while (g>0):
    k = f.read(g)
    if k == op :
        r = r + 1
    g = g - 1
r = r - 1
print ("to va8os twn leksikwn einai", r )
f.close()  