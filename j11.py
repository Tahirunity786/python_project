#                         THIS FILE IS BASED ON THE OPERATOR

#                  THERE ARE TWO six TYPE OF OPERATOR IN OPERATOR

# 1 ----- Arithmatic Operator
# 2 ----- Assignment operator
# 3 ----- Python comparison operator
# 4 ----- Bitwise operator
# 5 ----- LOGICAL OPERATOR
# 6 ----- Membership Operator

#                                 We Discuss the first point right now

var1 = 12 + 69.5
var2 = 12 - 70.5
var3 = 13 * 40
var4 = 2 ** 4  # THIS OPERATOR IS BASED ON THE 2*2*2*2 = 16
var6 = 78 / 7
var5 = 80 // 9  # THIS OPERATOR IS BASED ON, WHEN THE DIVISION HAS OCCURRED THE VALUE WILL ROUND OFF

print(var1, var2, var3, var4, var6, var5)

#                              NOW WE ARE WORKING IN (SECOND)ASSIGNMENT OPERATOR

var6 = 786  # ASSIGN THE 786
var7 = 86
var7 += 786
var8 = 75
var8 -= 786
var9 = 45
var9 *= 786
var10 = 10
var10 /= 5
var11 = 80
var11 %= 3
var12 = 66
var12 //= 7
var13 = 4
var13 **= 4
# Many other operator or less usability

#                                   NOW WE MOVE ON THE COMPARISON OPERATOR

if 10 > 9:  # This is GREATER THAN OPERATOR
    print("10 is greater than 9")
elif 10 < 9:
    print("10 is less than 9")
elif 9 == 9:
    print("9 is equal to 9")
else:
    print("FALSE")

print(10>=9)
print(10<=9)
print(10!=9)

#                                  LOGICAL OPERATOR ARE VERY EASY IN PYTHON
# 1   - and (operator)
# 2   - or (operator)
# 3   - not (operator)
x = 5
print(x > 3 and x < 10)
print(not(x > 3 and x < 10))
print(x > 3 or x < 4)
#                                          MEMBERSHIP OPERATORS
#  1 - in (operator)
#  2 - not in (operator)

#                                            BITWISE OPERATOR
# & 	AND	Sets each bit to 1 if both bits are 1
# |	    OR	Sets each bit to 1 if one of two bits is 1
# ^	    XOR	Sets each bit to 1 if only one of two bits is 1
# ~	    NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
