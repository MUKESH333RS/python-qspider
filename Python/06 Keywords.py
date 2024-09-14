"""
Keywords:
    - Keywords are the statements which have special meaning to the python.
    - Keywords are reserved words which had its own functionality.
    - There are totally 35 keywords in python.
    Syntax:
        import keyword
        keyword.kwlist
"""
import keyword
print(keyword.kwlist)

# ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await',
#  'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except',
#  'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

'''
Special Keyword:
    * There are 3 special keywords which are starting with upper key alphabet.
        - False
        - True 
        - None
        where we can use them as a value for the variable.
'''

'''
Soft Keywords:
    * These are the words which can be used as a variable name for the values.
    Syntax:
        import keyword
        keyword.softkwlist
'''
print(keyword.softkwlist)

# ['_', 'case', 'match']
# In old version ['type'] is also a soft keywords.


