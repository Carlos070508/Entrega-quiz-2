#Operadores Logicos
num1 = 5
num2 = 10

#and
print(num1 < 10 and num2 > 5) #1 1 = 1
print(num1 < 10 and num2 < 5) #1 0 = 0
print(num1 > 10 and num2 > 5) #0 1 = 0
print(num1 > 10 and num2 < 5) #0 0 = 0

#or
print(num1 < 10 or num2 > 5) #1 1 = 1
print(num1 < 10 or num2 < 5) #1 0 = 1
print(num1 > 10 or num2 > 5) #0 1 = 1
print(num1 > 10 or num2 < 5) #0 0 = 0

