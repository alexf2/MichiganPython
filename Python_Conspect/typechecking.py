# возможность проверки типов по аннотациям в рантайме
# pip install typeguard
from typeguard import typechecked


@typechecked
def vv(a: int) -> str:
    return str(a)


print(vv(11))
print(vv(11.2))
