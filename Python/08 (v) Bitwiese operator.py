# Bitwise operator
"""
=> (& - bitwise and
    | - bitwise or
    ~ - bitwise not
    ^ - bitwise xor
    << - bitwise left shift operator
    >> - bitwise right shift operator)

-> When we use bitwise operator, the operand is converted into its binary format and bit by bit operations is performed based on the operands.
-> Since the operands are connected to the binary format or it can be use only integers.
"""

# Bitwise and(&):
"""
-> When we use and(&) bitwise operator, the operand is converted into its binary format and bit by bit and(&) operations is performed based on the operands.
"""
# Example
print(16 & 12)                      # 0
print(120 & 17)                     # 16
print(20 & 81)                      # 16

# Bitwise or(|):
"""
-> When we use or(|) bitwise operator, the operand is converted into its binary format and bit by bit or(|) operations is performed based on the operands.
"""
# Example
print(20 | 10)                      # 30
print(18 | 22)                      # 22
print(102 | 65)                     # 103

# Bitwise not(~):
"""
-> When we use not(~) bitwise operator, the operand is converted into its binary format and bit by bit not(~) operations is performed based on the operands.
"""
# Example
print(~20)                          # -21
print(~-12)                         # 11
print(~124)                         # -125

# Bitwise xor(^):
"""
-> Here the operands are converted to its binary format and performed bit by bit operation and returns True when the input are different else False .
"""
# Example
print(15 ^ 8)                       # 7
print(29 ^ 17)                      # 12
print(120 ^ 27)                     # 99

# bitwise left shift operator(>>):
"""
-> Here hte first operand is converted to its binary format and the number of zero added at the end which is equal to the second operand.
"""
# Example
print(34 << 3)                      # 272
print(129 << 0)                     # 129
print(4 << 8)                       # 1024

# bitwise right shift operator(<<):
"""
-> Here hte first operand is converted to its binary format and the number of number of bits cancelled from right hand side(RHS) which is equal to the second operand.
"""
# Example
print(11 >> 3)                      # 1
print(36 >> 4)                      # 2
print(27 >> 6)                      # 0




