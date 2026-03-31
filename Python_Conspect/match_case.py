# сопоставление с образцами
def test(val):
    match val:
        case int(x):
            return 'int'
        case float(x):
            return 'float'
        case str(x):
            return 'str'
        case bool(x):
            return 'bool'
        case list(x):
            return 'list'
        case _:
            return type(val)


print(test(1))
print(test(1.2))
print(test('abc'))
print(test(True))
print(test([1, 2]))
print(test((1, )))
