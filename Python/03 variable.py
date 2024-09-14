'''Variable:
    - It is a name given to the memory location.
    - it is a container which is used to store the values.
    Syntax:
        variable_name = value

    * memory allocation for variable

        a = 171
        a = 10
        b = 10

    * once we create a variable, memory will be having two parts,
        - variable space / stack space
        - value space / heap space

        * First value will be stored in the value space, addr will be given for that block,
          that addr will be shared with respect to variable name in a variable space.

    id():
        - It is a inbuilt function, which is used to get the actual address of the value.
        Syntax:
            id(variable_name)

'''

a = 171
print(id(a))                # 140729641916520
a = 10
b = 10
print(id(a))                # 140729671271496
print(id(b))                # 140729671271496
