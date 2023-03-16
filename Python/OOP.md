## Концепция ООП простыми словами
Классы могут содержать свойства и методы

Инкапсуляция - работа с классом осуществляется только через разрешенные
свойства и методы, остальные свойства и методы скрыты

Наследование - общие свойства и методы выносятся в класс родитель, а 
производные от родителя их наследуют.
Благодаря этому мы можем использовать раннее созданные классы и расширять их 
функциональность.

Полиморфизм - возможность через единый интерфейс работать с объектами разных
классов

ad hoc - реализовывался через перегрузку функций и приведение различных типов
данных

параметрический
```python
class Figure:
    coords = None
    width = None
    color = None

    def draw(self):
        ...

class Line(Figure):
    def draw(self):
        ...

class Rectangle(Figure):
    def draw(self):
        ...

class Elipse(Figure):
    def draw(self):
        ...
```
Если у нас есть список объектов `Line, Rectangle, Elipse`, чтобы их отрисовать
без полиморфизма нам нужно было бы перебрать список каждого типа и вызвать
метод `draw()`.
С использованием полиморфизма нужно создать единый список, привести 
объекты к типу Figure и дальше когда будет вызываться метод draw(),
будет использоваться переопределенный метод.

#### Полиморфизм функций
```python
print(len("ООП-программирование"))
print(len(["Python", "Java", "C#", "Scala", "C++"]))
print(len({"Где изучить?": "В Otus", "Как проходят занятия?": "Онлайн"}))
-> 20
-> 5
-> 2
```
#### Полиморфизм в методах класса
```python
class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a cat. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Meow")


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"I am a dog. My name is {self.name}. I am {self.age} years old.")

    def make_sound(self):
        print("Bark")


cat1 = Cat("Kitty", 2.5)
dog1 = Dog("Fluffy", 4)

for animal in (cat1, dog1):
    animal.make_sound()
    animal.info()
    animal.make_sound()

-> Meow
-> I am a cat. My name is Kitty. I am 2.5 years old.
-> Meow
-> Bark
-> I am a dog. My name is Fluffy. I am 4 years old.
-> Bark
```
#### Переопределение метода (Полиморфизм и наследование)
```python
from math import pi


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        pass

    def fact(self):
        return "I am a two-dimensional shape."

    def __str__(self):
        return self.name


class Square(Shape):
    def __init__(self, length):
        super().__init__("Square")
        self.length = length

    def area(self):
        return self.length**2

    def fact(self):
        return "Squares have each angle equal to 90 degrees."


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return pi*self.radius**2


a = Square(4)
b = Circle(7)
print(b)
print(b.fact())
print(a.fact())
print(b.area())

-> Circle
-> I am a two-dimensional shape.
-> Squares have each angle equal to 90 degrees.
-> 153.93804002589985
```