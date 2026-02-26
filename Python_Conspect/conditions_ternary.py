# x = true_value if condition else false_value

def check_query(query):
    # Допишите код тела функции
    parts = query.split(', ')
    elements = ('', parts[0])[len(parts) > 0]  # тернарная операция
    if elements == 'Анфиса':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'


def check_query2(query):
    # Допишите код тела функции
    parts = query.split(', ')
    elements = parts[0] if len(parts) > 0 else ''  # тернарная операция
    if elements == 'Анфиса':
        return 'запрос к Анфисе'
    else:
        return 'запрос к кому-то ещё'


print(check_query(''))
print(check_query2(''))
print(check_query('Анфиса, который час'))
print(check_query2('Анфиса, который час'))
