# a is the initial number of infected students
a = 5
# b is the growth rate
b = 0.4
# n is the total number of infected students
n = 91
# c is the number of infected students in each day
c = a
m = 1
# m is the number of day
print ("the number of infected students in day "+ str(m) + " is " + str(c))
while c < n:
# if the number of infected students is smaller than the total number of studnets
    m = m + 1
# day +1
    c = c * (1+b)
# the number of infected students the day = (1 + c) * the number of infected students the last day
    if c >= 91:
# if all students are infected
        c = n
    print ("the number of infected students in day " + str(m) + " is " + str(c))
    if c == 91:
        print ("It takes " + str(m) + " days to infect all students")
        break
