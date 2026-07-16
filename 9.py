
#write a function that count vowels in string .

x= str(input("entre the string "))
check= x.count('a')+ x.count('e')+x.count('i')+x.count('o')+x.count('u')+x.count('A')+x.count('E')+x.count('I')+x.count('O')+x.count('U')
print("vowels count= " ,check)

# Using for loop :

text=str(input("entre the string"))
vowels="aeiouAEIOU"
count=0
for char in text:
    if char in vowels:
        count=count+1
print("vowels count:",count)
