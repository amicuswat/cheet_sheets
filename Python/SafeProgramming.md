## Типизация в Python: mypy, typing, linting

### mypy
Анотация функций
```python
def create_project(
        self,
        session: Session,
        title: str,
        actor_profile: Profile,
        members: List[Profile]
) -> Project:
    pass
```
PEP 484

Type Alias

```python
Vector = list[float]

def foo(factor: float, vector: Vector):
    pass
```

New Type
```python
from typing import NewType

UserId = NewType('UserId', int)

def get_username(user_id: UserId):
    pass
# т.е. если попытаться передать теперь в функцию просто int то будет ошибка. 
# должен передаваться именно UserId
```
PEP 526

PEP 589

TypedDict
```python
from typing import TypedDict

class Point2D(TypedDict):
    x: int
    y: int
    lable: str

a: Point2D = {'x': 1, 'y': 2, 'label': 'Good'}  # ok
b: Point2D = {'z': 3, 'lable': 'Bad'}           # Fails type check
```
Установить mypy
`pip install mypy`

## Unit tests в Python: легкий старт с нуля
Дока по [unittest](https://docs.python.org/3/library/unittest.html)

`python -m unittest discover {folder} # . для текущей папки`
