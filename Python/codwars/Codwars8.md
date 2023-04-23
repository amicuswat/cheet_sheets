# How much water do I need?

### Instruction
My washing machine uses water amount of water to wash load (in JavaScript and Python) or max_load (in Ruby) amount of clothes. You are given a clothes amount of clothes to wash. For each single item of clothes above the load, the washing machine will use 10% more water (multiplicative) to clean.

For example, if the load is 10, the amount of water it requires is 5 and the amount of clothes to wash is 14, then you need 5 * 1.1 ^ (14 - 10) amount of water.

Write a function howMuchWater (JS)/how_much_water (Python and Ruby) to work out how much water is needed if you have a clothes amount of clothes. The function will accept 3 arguments: - water, load (or max_loadin Ruby) and clothes.

My washing machine is an old model that can only handle double the amount of load (or max_load). If the amount of clothes is more than 2 times the standard amount of load (max_load), return 'Too much clothes'. The washing machine also cannot handle any amount of clothes less than load (max_load). If that is the case, return 'Not enough clothes'.

The answer should be rounded to the nearest 2 decimal places.
### Test
```python
def test_case():
    test.assert_equals(assert_return(how_much_water(10,10,21)), 'Too much clothes', "water = 10, load = 10, clothes = 21")
    test.assert_equals(how_much_water(10,10,2), 'Not enough clothes', "water = 10, load = 10, clothes = 2")
    test.assert_equals(how_much_water(10,11,20), 23.58, "water = 10, load = 11, clothes = 20")
    test.assert_equals(how_much_water(50,15,29), 189.87, "water = 20, load = 15, clothes = 29")

```

### My variant
```python
def how_much_water(water, load, clothes):
    if clothes <= load:
        return 'Not enough clothes'
    
    if clothes > load * 2:
        return 'Too much clothes'
    return round(water * 1.1 ** (clothes - load), 2)
```

### Other variants
```python

```

## Find Nearest square number

### Instruction
Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.

For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.

If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.
### Test
```python
def fixed_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(nearest_sq(1), 1)
        test.assert_equals(nearest_sq(2), 1)
        test.assert_equals(nearest_sq(10), 9)
        test.assert_equals(nearest_sq(111), 121)
        test.assert_equals(nearest_sq(9999), 10000)
```

### My variant
```python
def nearest_sq(n):
    sqrt = int(n ** 0.5)
    if abs(sqrt ** 2 - n) <  abs((sqrt + 1) ** 2 - n):
        return sqrt ** 2
    else:
        return (sqrt + 1) ** 2
```

### Other variants
```python
def nearest_sq(n):
    return round(n ** 0.5) ** 2
```
Автор просто округлил результат вычисления квадратного корня и возвел в квадрат.


## Count the number of cubes with paint on

### Instruction
Upon arriving at an interview, you are presented with a solid blue cube. The cube is then dipped in red paint, coating the entire surface of the cube. The interviewer then proceeds to cut through the cube in all three dimensions a certain number of times.

Your function takes as parameter the number of times the cube has been cut. You must return the number of smaller cubes created by the cuts that have at least one red face.

To make it clearer, the picture below represents the cube after (from left to right) 0, 1 and 2 cuts have been made.

### Test
```python
def example_tests():
    
    @test.it("For very few cuts")
    def example_tests():
        test.assert_equals(count_squares(5), 152)
        test.assert_equals(count_squares(16), 1538)
        test.assert_equals(count_squares(23), 3176)
```

### My variant
```python
def count_squares(cuts):
    angle_cubes = 8
    
    if not cuts:
        return 1
    
    if cuts == 1:
        return angle_cubes
    
    edge_cubes = 12 * (cuts - 1)
    plane_cubes = (cuts - 1) ** 2 * 6
    
    return angle_cubes + edge_cubes + plane_cubes
```

### Other variants
```python
def count_squares(x):
    return  (x + 1) ** 3 - (x - 1) ** 3
```
Формула не учитывает 0 разрезов - хотя в примере с условиями такой вариант приводится.
По сути формула считает все кубы и вычитает кубы которые внутри.

```python
def count_squares(cuts):
    return 1 if cuts == 0 else (cuts+1)*(cuts+1)*(cuts+1) - (cuts-1)*(cuts-1)*(cuts-1)
```
По сути тоже самое что предыдущая, только учитывае ситуацию с 0 разрезов

## Determine offspring sex based on genes XX and XY chromosomes

### Instruction
The male gametes or sperm cells in humans and other mammals are heterogametic and contain one of two types of sex chromosomes. They are either X or Y. The female gametes or eggs however, contain only the X sex chromosome and are homogametic.

The sperm cell determines the sex of an individual in this case. If a sperm cell containing an X chromosome fertilizes an egg, the resulting zygote will be XX or female. If the sperm cell contains a Y chromosome, then the resulting zygote will be XY or male.

Determine if the sex of the offspring will be male or female based on the X or Y chromosome present in the male's sperm.

If the sperm contains the X chromosome, return "Congratulations! You're going to have a daughter."; If the sperm contains the Y chromosome, return "Congratulations! You're going to have a son.";
### Test
```python
def basic_tests():
    test.assert_equals(chromosome_check('XY'), 'Congratulations! You\'re going to have a son.')
    test.assert_equals(chromosome_check('XX'), 'Congratulations! You\'re going to have a daughter.')
```

### My variant
```python
def chromosome_check(sperm):
    son = 'Congratulations! You\'re going to have a son.'
    daughter = 'Congratulations! You\'re going to have a daughter.'
    return son if 'Y' in sperm else daughter
```

### Other variants
```python
def chromosome_check(sperm):
    return 'Congratulations! You\'re going to have a {}.'.format('son' if 'Y' in sperm else 'daughter')
```
Решение похоже на мое, только автор оптимизировал работу со срокой
