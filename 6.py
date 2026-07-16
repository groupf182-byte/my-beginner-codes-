#mathmetical concepts :
#Calculate Mass ,Density or Volume:


choice= input("what do you want to calculate?( mass , density or volume ):")
if choice == "mass":
    d=float(input("entre the density of object:"))
    v=float(input("entre the volume of object :"))
    print("mass of the object =" ,d*v)
elif choice == "volume" :
    m=float(input("entre the mass of object    :"))
    d=float(input("entre the density of object:"))
    print("volume of the object =",m/d)
else :                                                  
    m=float(input("entre the mass of object    :"))
    v=float(input("entre the volume of object:"))
    print("volume of the object =",m/v)
