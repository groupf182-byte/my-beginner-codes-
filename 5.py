#Checking the divisibility of one integer by another.
first= int(input("entre the first integer :"))
second= int(input("entre the second integer :"))

if first%second ==0:
    print(f'{first}is completely divisible by {second}.Reminder = 0')
else:
    print(f'{first}is not completely divisible by {second}.Reminder is',first//second)


