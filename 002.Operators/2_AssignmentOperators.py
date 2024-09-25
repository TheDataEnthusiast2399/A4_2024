# Assignment Operators-
"""Assignment operators are used to assign values to variables:
=   --> a = 2
+=  --> a += 2 --> a = a + 2
-=  --> a -= 2 --> a = a - 2
/=  --> a /= 2 --> a = a / 2
*=  --> a *= 2 --> a = a * 2
%=  --> a %= 2 --> a = a % 2
**= --> a ** = 2 --> a = a ** 2

"""
a = 2
print("Equals to", a)
a += 3
print("Addition :", a)
a -= 1
print("Subtraction :", a)
a *= 5
print("Multiplication :", a)
a /= 4
print("Floor Division: ", a)
a %= 3
print(f"Remainder Division:{a:.0f}")
a **= 4
print(f"Eaponent:{a:.0f}")
