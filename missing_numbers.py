#y = input("enter list:")
#def missing_numbers(num_list):
 #   original_list = [x for x in range(num_list[0],num_list[-1] + 1 ) ]
 #   num_list = set(num_list)
 #   return(list(num_list ^ set(original_list)))
#print(missing_numbers(y))
list = [1,2,4,6,7,9]
def list_sort(y):
    num_list = []
    for x in range(1,9):
        if x not in  list:
            num_list.append(x)
    return num_list
print(list_sort(list))
        