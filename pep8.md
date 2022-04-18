# PEP8 Notes


## Whitespace in Expressions and Statements

### List Slicing

In a slice, the colon acts like a binary operator, and should have equal amounts of spacing
on either side (treating it as the operator with the lowest priority).

In an extended slice, both colons must have the same amount of spacing applied. The exception
is when a slice parameter is omitted:
```python
# Correct:
ham[1:9], ham[1:9:3], ham[:9:3], ham[1::3], ham[1:9:]
ham[lower:upper], ham[lower:upper:], ham[lower::step]
ham[lower+offset : upper+offset]
ham[: upper_fn(x) : step_fn(x)], ham[:: step_fn(x)]
ham[lower + offset : upper + offset]

# Wrong:
ham[lower + offset:upper + offset]
ham[1: 9], ham[1 :9], ham[1:9 :3]
ham[lower : : upper]
ham[ : upper]
```

### Other Binary Operators
If operators with different priorities are used, consider adding whitespace around operators
with the lowest priority(ies). Never use more than one space, and always have the same amount
of whitespace around both sides of a binary operator.
```python
# Correct:
i = i + 1
submitted += 1
x = x*2 - 1
hypot2 = x*x + y*y
c = (a+b) * (a-b)

# Wrong:
i=i+1
submitted +=1
x = x * 2 - 1
hypot2 = x * x + y * y
c = (a + b) * (a - b)
```

### Function Annotations
Don't use spaces when used to indicate a keyword argument, or when used to indicate a default value
for an *unannottated* function parameter. When combining an argument annotation with a default
value, then use spaces around the = sign.

```python
# Correct:
def complex(real, imag=0.0):
    return magic(r=real, i=imag)

def munge(sep: AnyStr = None): ...
def munge(input: AnyStr, sep: AnyStr = None, limit=1000): ...

# Wrong:
def complex(real, imag = 0.0):
    return magic(r = real, i = imag)

def munge(input: AnyStr=None): ...
def munge(input: AnyStr, limit = 1000): ...
```


### Compound Statements
Compound statements, or multiple statements on the same line, are generally discouraged:

```python
# Correct:
if foo == 'blah':
    do_blah_thing()
do_one()
do_two()
do_three()

# Wrong:
if foo == 'blah': do_blah_thing()
do_one(); do_two(); do_three()
```


### Docstrings
For functions, comments should always appear after the `def` line. Most importantly, the """ that
ends a multiline docstring should be on a line by itself.

For oneliner docstrings, keep the closing """ on the same line.
```python
"""Return a foobang

Optional plotz says to frobnicate the bizbaz first.
"""

"""Return an ex-parrot."""
```