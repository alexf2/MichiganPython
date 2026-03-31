import json
from dataclasses import asdict, dataclass


@dataclass
class User:
    name: str
    age: int


test_users = (User('Ivan', 32), User('Alex', 42), User('Anna', 29))
test_users = sorted(test_users, key=lambda u: u.age)

# user_str = json.dumps(list(map(lambda u: asdict(u), test_users)), indent=2, ensure_ascii=False)
# dumps сериализует dict, поэтому, преобразуем объекты в dict
user_str = json.dumps([asdict(u) for u in test_users], indent=2, ensure_ascii=False)

print(user_str)

# loads возвращает словари
users = (User(**u) for u in json.loads(user_str))

print(list(users))
