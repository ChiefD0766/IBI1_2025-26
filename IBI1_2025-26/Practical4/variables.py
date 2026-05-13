a=5.08
b=5.33
c=5.55
d=b-a
e=c-b
if d>e:
    print("d is larger than e")
if e>d:
    print("e is larger than d")
if e==d:
    print("e is equal to d")
#d is larger than e; the population growth is decelerating in Scotland
X = True
Y = False
W = X or Y
print(W)
#X     Y     W
#True  False True
#True  True  True
#False True  True
#False False False