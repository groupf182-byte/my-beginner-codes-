# Is there a triangle with given sides exists or not ?
'''A triangle is exists only if:
the sum of any two sides of tringle is
must be greater than the third side .
for all three sides .'''
print('we will check whether the given triangle is exists or not:')
x= float(input('entre the first side :'))
y=float(input('entre the second side:'))
z=float(input('entre the third side:'))

if x+y>z and y+z>x and z+x>y :
    print("Given triangle exists ")
elif x+y==z and y+z==x and z+x==y :
    print (" Out of my knowledge ")
else :
    print("Given triangle dosen't exists")
