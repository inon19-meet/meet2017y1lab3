Python 3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609] on linux
Type "copyright", "credits" or "license()" for more information.
>>> a = 4
>>> b = 'panda bears'
>>> print(a + b)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    print(a + b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str()
''
>>> str(a + b)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    str(a + b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(a)
'4'
>>> print(a + b)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print(a + b)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> print(str(a) + b)
4panda bears
>>> print(str (a) + " " + b)
4 panda bears
>>> test=' I" " Love " " MEET)
SyntaxError: EOL while scanning string literal
>>> TEST='I " " Love " " MEET')
SyntaxError: invalid syntax
>>> "I love MEET"
'I love MEET'
>>> n = "inon rawan"
>>> len(n)
10
>>> len(n * 1000)
10000
>>> pritn(n * 1000)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    pritn(n * 1000)
NameError: name 'pritn' is not defined
>>> a = 5
>>> a
5
>>> print(a)
5
>>> upper(" i love meet")
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    upper(" i love meet")
NameError: name 'upper' is not defined
>>> upper(a)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    upper(a)
NameError: name 'upper' is not defined
>>> s = "hello moto koto roto"
>>> s.replace("o", "j")
'hellj mjtj kjtj rjtj'
>>> s
'hello moto koto roto'
>>> s.upper("o","k")
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    s.upper("o","k")
TypeError: upper() takes no arguments (2 given)
>>> s.upper("o")
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    s.upper("o")
TypeError: upper() takes no arguments (1 given)
>>> s.upper()
'HELLO MOTO KOTO ROTO'
>>> s.lower()
'hello moto koto roto'
>>> s.capitalize()
'Hello moto koto roto'
>>> s.swapase()
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    s.swapase()
AttributeError: 'str' object has no attribute 'swapase'
>>> s.swapcase()
'HELLO MOTO KOTO ROTO'
>>> s.swapcase()
'HELLO MOTO KOTO ROTO'
>>> a = "MEET"
>>> a.swapcase()
'meet'
>>> a = "MEET"
>>> b = "meet"
>>> c = "Meet"
>>> a == b
False
>>> a ==c
False
>>> b == c
False
>>> a != b
True
>>> a != c
True
>>> b != c
True
>>> b =! c
SyntaxError: invalid syntax
>>> a =! b
SyntaxError: invalid syntax
>>> a = b
>>> a ==b
True
>>> a
'meet'
>>> b
'meet'
>>> c
'Meet'
>>> my_string = “bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: invalid character in identifier
>>> my_string = "bananayellowthinkhatgreyBIGcalifornia314”
SyntaxError: EOL while scanning string literal
>>> my_string = "bananayellowthinkhatgreyBIGcalifornia314"
>>> my_string[6]
'y'
>>> my_string[8]
'l'
>>> my_string[10]
'o'
>>> my_string[12]
't'
>>> my_string[15]
'n'
>>> my_string[16]
'k'
>>> my_string[12:16]
'thin'
>>> my_string[12:17]
'think'
>>> my_string[20]
'g'
>>> my_string[24]
'B'
>>> my_string[27]
'c'
>>> my_string[12:17] + my_string[24:27]
'thinkBIG'
>>> my_string[12:17]+" "+ my_string[24:27]
'think BIG'
>>> example = "Think big"
>>> amir = my_string[12:17]+" "+ my_string[24:27]
>>> amir
'think BIG'
>>> amir.capitalize()
'Think big'
>>> amir.replace("i","o")
'thonk BIG'
>>> amir.replace("i","o") amir replace ("I","O")
SyntaxError: invalid syntax
>>> amir
'think BIG'
>>> amir = amir.replace("i","o")
>>> amir
'thonk BIG'
>>> amir = amir.replace("I", "O")
>>> amir
'thonk BOG'
>>> 
