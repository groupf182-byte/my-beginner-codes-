#Reverse full name.
name=input("entre your name")
print(name[::-1])

# another method (without changing meaning).
name=input("entre your name")
list1= name.split()[::-1]   #[::-1] why?
print('converted to list:',list1)
        #mere name ko split kar dega according to given input,
        #aur list mai convert kar dega.
reverse=" ".join(list1)
print("Now,reverse form will be :" ,end="")
print(reverse)
