**NUMBER**
**********
#Modulo
 7 mod 4 = 7 % 4 in python

#Powers
2^3 = 2**3 in python

#Python Dynamic Typing
This means you can reassign variables to different data types.
This makes python very flexible in assigning data types, this is different from other languages that use *Statically-Typed*

**STRINGs**
You can use both single quotes or double quotes.

**Slicing**
This allows you to grab a subsection of multiple characters, a "slice" of the string. This has the followinf syntax *[start:stop:step]*
*start*: is a numerical index for the slice start
*stop*: is the index you would go up to(but not to include)
*step*: is the size of the "jump" you take. from start to stop

**Escape Sequence**:This allows you to characters as a new line or tab space:
i.e 1 --> *print("hello \n world ")*
#output:
hello
world
i.e 2 --> *print("hello \tworld ")*
#output: hello  world

**LENGHT FUNCTION**: this allows you to check the length of a string
i.e 2 --> *print(len("this is sweet"))*
#output: 13

**Indexing with strings**
i.e --> *mystring = "Hello World"*
lets grab a single char from the string  i.e "r"
i.e --> *print(mystring[8])*
#output: r

**Reverse Indexing with strings**
i.e --> *mystring = "Hello World"*
lets grab a single char from the string  i.e "r"
you would start counting back from -1 from the end of the string
i.e --> *print(mystring[-3])*
#output: r

**Slicing with strings1**
i.e --> *mystring = "abcdefghijk"*
Note: remember the syntax from slicing *[start:stop:step]*
i.e --> lets grab between "c" to "j":
*print(mystring[3:-2])*
#output: defghi

**Slicing with strings2**
i.e --> lets grab from "c" all the way to the end
*print(mystring[2:])*
#output: cdefghijk

**Slicing with strings3**
i.e --> lets grab from begining to a specific point i.e ("g")
*print(mystring[:6])*
#output: abcdef

**Slicing with strings4**
i.e --> lets grab the entire string
*print(mystring)* or *print(mystring[::])*
#output: abcdefghijk

**Slicing with strings using step size**
i.e --> lets grab using step size of 2
*print(mystring[::2])*
#output: acegik

**Slicing with strings using Start:Stop:step size**
i.e --> *mystring = "abcdefghijk"*
i.e --> lets grab using step size of 2
*print(mystring[1:7:2])*
#output: bdf

**Reverse String using step size**
i.e --> *mystring = "abcdefghijk"*
*print(mystring[::-1])*
#output:kjihgfedcba

**String Properties and Methods**
String Immutability: cannot mutate or change
i.e. --> *name="Sam"*
if you try--> *name[0]= "P"*
#output: Error:
'str' object does not support item assignment
Note: To change that we have create a new strings or concatenate the current string
i.e. --> *letters[1:]*
--> *name ="P"+ letters*
--> *print(name)*

**Objects in Python**
Note: objects in Python usually have built in method, these methods are functions that are essentially inside the objects.   
i.e. --> *X ="Hey There"*
     --> *X.hitTabBtn* --> This should show you a list of attributes/Methods

**Using the upper case function**
i.e. --> *X ="Hey There"*
     --> *print(X.upper())*
#output --> *HEY THERE*

**Using the lower case function**
i.e. --> *X ="HEY THERE"*
     --> *print(X.lower())*
#output --> *hey there*

**Using the split function**
Note: This helps you to create a list out of a string and will split a string based on the white space.
i.e. --> *X ="Hey There Please Split My Sausage"*
     --> *print(X.split())*
#output --> *['Hey', 'There', 'Please', 'Split', 'My', 'Sausage']*

**Using the split function to split base on characters**
Note: This helps you to create a list out of a string and will split a string based on a letter or whitespace. 
i.e. --> *X ="Hey There Please Split My Sausage"*
     --> *print(X.split(e))*
#output --> *['H', 'y Th', 'r', ' Pl', 'as', ' Split My Sausag', '']*

**Print formatting for Printing**
Note: we will format a string and print a variable in it, this is knoown as *String interpolation*
i.e. --> *.format()* method and the *f-string* (formatted string literals)
