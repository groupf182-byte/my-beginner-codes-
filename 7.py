#In which quadrant the given coodinates are lies :
x= int(input("entre the X coordinate :"))
y=int(input("entre the Y coordinate:"))

if x>0 and y>0 :
    print(f'Given coordinates {x,y}are lies in first quadrant')
elif x<0 and y>0 :
    print(f'Given coordinates {x,y}are lies in second quadrant')
elif x<0 and y<0 :
    print(f'Given coordinates {x,y}are lies in third quadrant')
else:
    print(f'Given coordinates {x,y}are lies in fourth quadrant')
