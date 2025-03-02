---
title: Binary operations
parent: Python notes
layout: default
nav_order: 6
---

# Binary operatiomns
{: .no_toc }

- TOC
{:toc} 

This assumes you understand binary and other number systems and the operations involved.

To assign binary or hexadecimal values to an integer

```py
number = 0b101010   # 42
number = 0x2a       # 42
```

Convert string representation of binary or hexadecimal values to integers

```py
number = int("101010", base=2)  # 42
number = int("2a", base=2)  # 42
```

Convert integer to string representation of binary or hexadecimal numbers

```py
print( bin( 42 ))               # '0b101010'
print( bin( 42 )[2:])           # '101010'
print( hex( 42 ))               # '0x2a'
print( hex( 42 )[2:])           # '2a'
```

Bit shifting

```py
number = 1 << 4
print(number) # 16 ... or binary 1000

number = 0b101110 >> 4
print(number) # 0b10 ... data is lost as bits shifted right!
```

Bit logic 

```py
# ... perform 'and' operation bit-by-bit
number = 64 & 8    # ie: number = 0b1000000 & 0b1000 ... result 0
number = 78 & 8    # ie: number = 0b1001110 & 0b1000 ... result 8
number = 78 & 15   # ie: number = 0b1001110 & 0b1111 ... result 14

# ... perform 'or' operation bit-by-bit
number = 78 | 15   # ie: number = 0b1001110 | 0b1111 ... result 79

# ... perform 'xor' operation bit-by-bit
number = 78 ^ 15   # ie: number = 0b1001110 ^ 0b1111 ... result 65

# ... perform 'not' operation bit-by-bit... check: 2s complement
number = ~78       # ... result -79
```
