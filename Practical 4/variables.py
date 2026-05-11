a = 5.08
b = 5.33
c = 5.55
d = b - a
# d is the population growth from 2004 to 2014
e = c - b
# e is the population growth from 2014 to 2024
# d = 0.25 & e = 0.22, d > e, the population growth is decelerating
if e > d:
    print ("population growth is accelerating")
# if e > d, the population growth of the current decade is larger then the last decade
elif d > e:
     print ("population growth is decelerating")
# if e < d, the population growth of the current decade is smaller then the last decade
else:
    print ("population growth is unchanged")
X = True 
Y = False
W = X or Y
# Truth table for W
#   X    |  Y    |   W
#  True  | True  |  True
#  True  | False |  True
#  False | True  |  True
#  False | False |  False
print (W)