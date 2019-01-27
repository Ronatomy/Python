year_of_birth = int(input("enter year_of_birth:"))
x = year_of_birth
if x > 2001:
    print("minor")
elif x > 1983:
    print("youth")
if x > 1900:
    print("elder") 
else:
    print("enter correct year of birth")    
    #if x < 1900:
      # print("Enter correct year of birth")   
#else:
    #print("elder")

