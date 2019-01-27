person = {"name":"john","email":"a@gmail.com","number":425356265}


all_contacts = [person]
# 1 collect data
name = input("enter your name:")
email = input("enter your email:")
number = int(input("enter number:"))

# 3 organise data
new_person = {"name":name,"email":email,"number":number}
all_contacts.append(new_person)

for x in all_contacts:
    print(x) 
#while x < 60:
    # x = 1
    #print(x)
    #x += 1
