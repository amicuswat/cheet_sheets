## Перенести 0 в конец списка 5 lv

### Тест
```python
@test.it("Basic tests")
def youarecute():
    test.assert_equals(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]),
        [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])
    test.assert_equals(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]),
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    test.assert_equals(move_zeros([0, 0]), [0, 0])
    test.assert_equals(move_zeros([0]), [0])
    test.assert_equals(move_zeros([]), [])
```

### Мое решение
```python
def move_zeros(lst):
    limit = len(lst)
    counter = 0
    while counter < limit:
        if not lst[counter]:
            del lst[counter]
            lst.append(0)
            limit -= 1
        else:
            counter += 1
    return lst
```

### Другие решения и их разбор
```python
def move_zeros(arr):
    l = [i for i in arr if isinstance(i, bool) or i!=0]
    return l+[0]*(len(arr)-len(l))
```
Здесь автор в l сохраняет в список не нулевые элементы
Находит разность между длинной оригинального списка и списка без нулей
Добавляет в конец списка без нулей, количество нулей равное разнице в длинне списков
Зачем автор добавил проверку на bool не понятно, по условиям bool не предполагалось
```python
def move_zeros(array):
    return sorted(array, key=lambda x: x==0 and type(x) is not bool)
```
Автор использовал сортировку, если элемент удовлетворяет условиям
ему присваивается 1 если нет то 0 следственно элементы с 1 попадают в 
конец списка а с 0 остаются на месте.

```python
def move_zeros(array):
    for i in array:
        if i == 0:
            array.remove(i) # Remove the element from the array
            array.append(i) # Append the element to the end
    return array
```
Автор убирает из списка элемент 0 если это 0 и добавляет его в конец списка
Максимально явное решение.
```python
def move_zeros(array):
    return [x for x in array if x] + [0]*array.count(0)
```