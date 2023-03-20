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



