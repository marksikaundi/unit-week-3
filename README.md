# Calculator in command line using python programming language
University of the People Python fundamental
# Chapter 5
Conditionals and recursion
The main topic of this chapter is the if statement, which executes different code depending
on the state of the program. But first I want to introduce two new operators: floor division
and modulus.
5.1 Floor division and modulus
The floor division operator, //, divides two numbers and rounds down to an integer. For
example, suppose the run time of a movie is 105 minutes. You might want to know how
long that is in hours. Conventional division returns a floating-point number:
>>> minutes = 105
>>> minutes / 60
1.75
But we don’t normally write hours with decimal points. Floor division returns the intege
To get the remainder, you could subtract off one hour in minutes:
>>> remainder = minutes - hours * 60
>>> remainder
45
An alternative is to use the modulus operator, %, which divides two numbers and returns
the remainder.
>>> remainder = minutes % 60
>>> remainder
45
The modulus operator is more useful than it seems. For example, you can check whether
one number is divisible by another—if x % y is zero, then x is divisible by y

If you are using Python 2, division works differently. The division operator, /, performs
floor division if both operands are integers, and floating-point division if either operand is
a float.
# 5.2 Boolean expressions
A boolean expression is an expression that is either true or false. The following examples
use the operator ==, which compares two operands and produces True if they are equal
and False otherwise:
>>> 5 == 5
True
>>> 5 == 6
False
True and False are special values that belong to the type bool; they are not strings:
>>> type(True)
<class 'bool'>
>>> type(False)
<class 'bool'>
The == operator is one of the relational operators; the others are:
x != y # x is not equal to y
x > y # x is greater than y
x < y # x is less than y
x >= y # x is greater than or equal to y
x <= y # x is less than or equal to y
Although these operations are probably familiar to you, the Python symbols are different
from the mathematical symbols. A common error is to use a single equal sign (=) instead of
a double equal sign (==). Remember that = is an assignment operator and == is a relational
operator. There is no such thing as =< or =>.
# 5.3 Logical operators
There are three logical operators: and, or, and not. The semantics (meaning) of these
operators is similar to their meaning in English. For example, x > 0 and x < 10 is true
only if x is greater than 0 and less than 10.
n%2 == 0 or n%3 == 0 is true if either or both of the conditions is true, that is, if the number
is divisible by 2 or 3.