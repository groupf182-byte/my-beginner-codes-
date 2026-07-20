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

"""
Explenatation:
The Key Insight
This code reverses a name by splitting words → reversing list order → rejoining. The [::-1] is Python slice notation meaning "start at end, go backwards, step -1" — it reverses a list in one compact expression.

What This Code Does
Takes a person's name and prints it in reversed word order. For "John Smith", it outputs "Smith John". This works for any number of name parts.

Flowchart## Understanding the Code
Why It Works This Way
The [::-1] trick:

list1 = [1, 2, 3]
list1[::-1] → [3, 2, 1] (reads backwards)
It's Python's shortcut for reversing sequences
Why split + reverse + join?

split() breaks string into list of words
[::-1] reverses the list order
join() puts it back together as string
Step-by-Step Breakdown
Line	What Happens	Example
1	User enters name	"John Smith"
2	split() → list	["John", "Smith"]
2	[::-1] → reversed	["Smith", "John"]
3	Print intermediate	shows reversed list
6	" ".join() → string	"Smith John"
7-8	Print final result	displays reversed name
Common Confusions
Why [::-1] and not reverse()?

reverse() modifies list IN PLACE and returns None
[::-1] creates a NEW reversed list
[::-1] is more readable for one-liners
What if only one name entered?

"John".split() → ["John"]
["John"][::-1] → ["John"] (no change)
Output is same as input """
