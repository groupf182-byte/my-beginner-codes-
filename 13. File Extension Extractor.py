''' Write a Python program that accepts a filename from the user
and prints the extension of the file.'''

filename= input("entre the file name")
f_split= filename.split(".")
#optional
#print(f_split)
f_ext=repr(f_split[-1])
print(f'the file extension of "{filename}" is :',f_ext)

'''Explanation 
The Key Insight
This code extracts a file extension by splitting the filename at the period and taking the last element. The last part after the dot is always the extension.

What This Code Does
Takes a filename from user input, separates it by the "." character, and displays the file extension (the portion after the last dot). This is a simple string manipulation exercise.

Flowchart## Understanding the Code
Why It Works This Way
split(".") breaks a string wherever it finds a period. For "photo.jpg", this creates ["photo", "jpg"]
f_extns[-1] accesses the last element using negative indexing. This works even if the filename has multiple dots like "archive.tar.gz" (returns "gz")
repr() shows the string with quotes, making it clear what was extracted (including if it's empty)
Step-by-Step Breakdown
Line 2: User types a filename like "document.pdf" - stored as a plain string
Line 5: "document.pdf".split(".") creates ["document", "pdf"] - a list with 2 elements
Line 8: f_extns[-1] gets "pdf" - the last item in the list, which is the extension
Common Confusions
split() returns a list, not just the extension
[-1] means "last element" - this is Python's negative indexing
If no dot exists (e.g., "filename"), the whole string becomes the only list element'''