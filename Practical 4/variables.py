a = 5.08
b = 5.33
c = 5.55
d = b-a
e = c-b
if e > d:
    print ("Population growth is accelerating in Scotland")
else :
    print ("Population growth is decelerating in Scotland")
X = True
Y = False
W = X or Y
print (W)

# Population growth is decelerating in Scotland
# Truth table for W 
# X = True , Y = False -> W = True
# X = True , Y = Flase -> W = True
# X = False , Y = True -> W = True
# X = False , Y = False -> W = False