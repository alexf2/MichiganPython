# 1. Упаковка и распаковка аргументов функции

# A sample python function that takes three arguments
# and prints them
def fun1(a, b, c):
    print(a, b, c)
 
# Another sample function.
# This is an example of PACKING. All arguments passed
# to fun2 are packed into tuple *args.
def fun2(*args):
 
    # Convert args tuple to a list so we can modify it
    args = list(args)
 
    # Modifying args
    args[0] = 'Geeksforgeeks'
    args[1] = 'awesome'
 
    # UNPACKING args and calling fun1()
    fun1(*args)
 
# Driver code
fun2('Hello', 'beautiful', 'world!')

# ------------------------------------------------------------

# Пример распаковки set в list
def get_together_games(list1: list[str], *lists: tuple[list[str], ...]) -> set[str]:
    return [*set(list1).intersection(set(*lists)), ]