# Write a Python program to find the string similarity between two given strings
str1 = input("Enter string 1: ")
str2 = input("Enter string 2: ")

len1 = len(str1)
len2 = len(str2)
matchCnt = 0
if len1>len2:
    long = len1
    short = len2
else:
    long = len2
    short = len1
for i in range(short):
    if(str1[i] == str2[i]):
        matchCnt+=1
print("The similarity between the two strings:",matchCnt/long)
