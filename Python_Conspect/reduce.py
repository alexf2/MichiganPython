import functools
import operator

# способы применения reduce
print(functools.reduce(lambda a, b: a + b, range(0, 10)))
print(functools.reduce(operator.add, range(0, 10)))

print(0+1+2+3+4+5+6+7+8+9)
