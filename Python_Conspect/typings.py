from typing import Dict, List, Optional


def add_by_note(items: Dict[str, List[Dict]], note: str) -> None:
    pass


# Необязательные аргументы

def greet(name='гость'):
    if not name == 'гость':
        return f'Привет, {name}!'
    return ''


# Функция greet() может вернуть строку или None,
# так что надо аннотировать переменную этими двумя типами.
result_no_name: Optional[str] = greet()
print(result_no_name)
