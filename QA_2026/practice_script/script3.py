# try:
#     print(5/1)
# except:
#     print("Print Exception")
from xml.parsers import expat

try:
    print(10/0)
except ZeroDivisionError:
    print("Division by zero")
except SyntaxError:
    print("Syntax error")
except:
    print("Other error")
else: # always executed when try is correct
    print("Else...")
finally: # always executed no matter whether we are in try or except
    print("Finally...")