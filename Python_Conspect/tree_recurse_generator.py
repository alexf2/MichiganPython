from pathlib import Path


def tree(path, level=0):
    path_obj = Path(path)
    # тут возвращаем последний компонент пути (папку)
    yield path_obj.name, level
    for dir in (item.name for item in path_obj.iterdir() if item.is_dir()):
        # тут уходим 
        sub_path = path_obj / dir
        # используем делегирующий генератор yield from
        yield from tree(sub_path, level + 1)


def display_dir(path):
    for name, level in tree(path):
        indent = ' ' * 4 * level
        print(f'{indent}{name}')


if __name__ == '__main__':
    display_dir('d:\\Tools')
