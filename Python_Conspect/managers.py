# with ContextManager as cm:
# Код, который будет выполнен в контексте ContextManager.


f = open('hello_bro.txt', 'w')
f.write('Здравствуй, Стас!')
f.close()

# или

with open('hello_bro.txt', 'w') as f:
    f.write('Здравствуй, Стас!')

# https://docs.python.org/3/library/contextlib.html
