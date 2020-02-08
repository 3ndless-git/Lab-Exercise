#N students take K apples and distribute them among each other evenly. The remaining
#the (undivisible) part remains in the basket. How many apples will each single student
#get? How many apples will remain in the basket? The program reads the numbers N and
#K. It should print the two answers for the questions above.
S =int(input("Enter the Number of Students:"))
A=int(input("Enter the Number of Apples:"))
X = A/S
Y = A%S
print(X)
print(Y)