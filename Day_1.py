Python 3.14.2 (tags/v3.14.2:df79316, Dec  5 2025, 17:18:21) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
s="shivani patil"
s
'shivani patil'
s.capitalize()
'Shivani patil'
s.upper()
'SHIVANI PATIL'
s
'shivani patil'
#String is Immutable data type in python
#Immutable means :-We cannot change original object
s
'shivani patil'
#In Python data type we have 2 options
#1.Mutable
#2.Immutable
#------------------------------------------------------------------
# hash is used for the comment
#Comment
#Different options for Python coding
#1.IDLE
#2.pycharm
#3.vs code
#4.Google colab Notebook
#From this industry mostly prefer vs code
#-------------------------------------------------------------
#Identifier:-a name given to the object
#Object:-is a physical entity present in the program/memory
#eg
100
100
"Python"
'Python'
4.55
4.55
x =100
#x is a identifier
#100 is an object
y = "Python"
y
'Python'
#y is an identifier
#python is object

#identifiers are also known as variables

#------------------------------------------------------------
#Rules of declaring an identifier
#a-zA-Z allowed
#_ is allowed
first name ='python'
SyntaxError: invalid syntax
first_name = 'python'
#space is not allowed uderscore(_) is allowed
first_name
'python'
'python'
'python'
>>> #special symbols and chars are not allowed
>>> #eg:-
>>> first&name='python'
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
>>> 
>>> first$name='python'
SyntaxError: invalid syntax
>>> #-----------------------------------------------------------------------------
>>> 
>>> #Number as a prefix not allowed
>>> #eg:-
>>> 1num=100
SyntaxError: invalid decimal literal
>>> 2_pin=123
SyntaxError: invalid decimal literal
>>> 
>>> #Number as a suffix is allowed
>>> #eg:-
>>> num1=100
>>> num1
100
>>> pin_2=123
>>> pin_2
123
>>> #---------------------------------------------------------------
>>> #dont use reserve keywords
>>> in=99
SyntaxError: invalid syntax
>>> #To Check reserve keyword we have keyword library
>>> import keyword
>>> import
SyntaxError: Expected one or more names after 'import'
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
>>> as=100
SyntaxError: invalid syntax
>>> len(keyword.kwlist)
35
