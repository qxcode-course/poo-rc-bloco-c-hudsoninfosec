import numpy as np
bolo = np.random.randint(1, 11, 9)

def buscar_elemento(a, c):
    if c in a:
        return f"{c} está na lista"
    else:
        return f"{c} não está na lista"
m = ["amor", "paz", "vida"]
l = ["maça", "banana", "ovo"]
l2 = list([2, 2, 4])
l2.append(3)
l.append("pera")
l.remove("pera")
l2.pop(2)
fofin = "-".join(l)
print (fofin)
print(l)
print(l2)
print(bolo)
puf = m[0]
c = int(input())
a = []
for _ in range(1, c+1):
    a.append(_)

for i in a:
    print(i)

for i in range(len(a)):
    print(i)

for i, v in enumerate(a):
    print(i, v)

ameba = buscar_elemento(a, c)
print(ameba)

print(a)
print(puf)

print("oi")