input ('''
We will  convert celcius to farenhit.
please entre to start''')

c= float(input("entre the celcius degree to convert____"))
f=9/5*c+32
print(f,end="\n" f'The {c}degree celcius into faranhate is equal to {f}degree faranhate ' )

input("""
Now we will convert Farenhate to Celcius.
Please entre to start___""")

x=float(input("entre the Farenhate degree to convert___"))
c=(x-32)*5/9
print(c,end="\n" f'The {x}degree faranhate is equal to {c}degree celcius ')
