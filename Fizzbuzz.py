list_1 = (input("enter list 1:"))
list_2 = (input("enter list 2:"))
if (len(list_1) + len(list_2)) % 3 == 0:
    print("Fizz")
elif (len(list_1) + len(list_2)) % 5 == 0:
    print("buzz")
elif (len(list_1) + len(list_2)) % 3 == 0 and (len(list_1) + len(list_2)) % 5 == 0:
    print("Fizzbuzz")  
else:
    print(len(list_1) + len(list_2))

