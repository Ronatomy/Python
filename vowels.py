x = str(input("Enter string:"))
list = []
for letter in x:
   if letter in ['a','e','i','o','u']:
    list.append(letter)
print(tuple(list))