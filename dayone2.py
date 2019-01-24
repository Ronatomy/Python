#thisdict = {"x":"x*x"}
x = 1
while x < 16:
    print(x)
    x += 1

    def my_function(x):
       return  x*x

    print(my_function(x))

    thisdict = {x:my_function(x)}
    print(thisdict)