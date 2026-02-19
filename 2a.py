# Write a Python program that accepts a sentence and 
# find the number of words, digits, uppercase letters, and lowercase letters.

sentence = input("Enter the sentence: ")
split_sentence = sentence.split()
print("The split() operation on sentence leads to:",str(split_sentence))
words = len(split_sentence)
digits = lowercase = uppercase = 0
for c in sentence:
    if c.isdigit():
        digits+=1
    elif c.islower():
        lowercase+=1
    elif c.isupper():
        uppercase+=1

print("Number of words:",words)
print("Number of digits:",digits)
print("Number of lowercase letters:",lowercase)
print("Number of uppercase letters:",uppercase)