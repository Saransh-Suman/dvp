# Develop a Python program to check whether a given number is palindrome or not and also count 
# the number of occurrences of each digit in the input number.

val = int(input("Enter the string: "))
str_val = str(val)
if(str_val == str_val[::-1]):
    print("Palindrome")
else:
    print("Not a palindrome")

for i in range(10):
    if(str_val.count(str(i))>0):
        print(str(i),"appears",str_val.count(str(i)),"times")
    