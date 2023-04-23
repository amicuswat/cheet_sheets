# Cats and shelves

### Instruction
Description
An infinite number of shelves are arranged one above the other in a staggered fashion.
The cat can jump either one or three shelves at a time: from shelf i to shelf i+1 or i+3 (the cat cannot climb on the shelf directly above its head), according to the illustration:
#### Input
Start and finish shelf numbers (always positive integers, finish no smaller than start)

#### Task
Find the minimum number of jumps to go from start to finish

#### Example
Start 1, finish 5, then answer is 2 (1 => 4 => 5 or 1 => 2 => 5)

### Test
```python
def test_group():
    @test.it("Example test case")
    def test_case():
        test.assert_equals(solution(1,5), 2)
    @test.it("One more test case")
    def test_case():
        test.assert_equals(solution(2,4), 2)
```

### My variant
```python
def solution(start, finish):
    return (finish - start) // 3 + (finish - start) % 3
```

### Other variants
```python
def solution(start, finish):
    return sum(divmod(finish-start, 3))
```
divmod(num, divider) - возвращает частное и остаток

## Mysterious Singularity Numbers

### Instruction
#### Task
The point is that a natural number N (1 <= N <= 10^9) is given. You need to write a function which finds the number of natural numbers not exceeding N and not divided by any of the numbers [2, 3, 5].

#### Example
Let's take the number 5 as an example:

1 - doesn't divide integer by 2, 3, and 5
2 - divides integer by 2
3 - divides integer by 3
4 - divides integer by 2
5 - divides integer by 5
Answer: 1

### Test
```python
def test_real_numbers():
        test.assert_equals(real_numbers(5), 1)
        test.assert_equals(real_numbers(10), 2)
        test.assert_equals(real_numbers(20), 6)
        test.assert_equals(real_numbers(30), 8)
        test.assert_equals(real_numbers(40), 10)
        test.assert_equals(real_numbers(55), 15)
        test.assert_equals(real_numbers(66), 17)
        test.assert_equals(real_numbers(75), 20)
        test.assert_equals(real_numbers(100), 26)
```

### My variant
```python
def real_numbers(n):
    return len([i for i in range(1, n+1) if (i % 2) and (i % 3) and (i % 5)])
```
Решение крашится изза производительности

### Other variants
```python
def real_numbers(n):
    return n - (n // 2 + n // 3 + n // 5 + n // 30) + (n // 6 + n // 10 + n // 15)
```
Не понимаю, как вывели такую формулу. 


## Valid Parentheses

### Instruction
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid. The function should return true if the string is valid, and false if it's invalid.

Examples
```python
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
```
### Test
```python
def valid_cases():
    run_test(True, "()")
    run_test(True, "((()))")
    run_test(True, "()()()")
    run_test(True, "(()())()")
    run_test(True, "()(())((()))(())()")
```

### My variant
```python
def valid_parentheses(paren_str):
    par_list = list(paren_str)
    
    while par_list:
        if len(par_list) == 1:
            return False
        
        try:
            if par_list.index('(') > 0:
                return False
        except ValueError:
            return False
        
        par_list.remove('(')
        
        try:
            par_list.remove(')')
        except ValueError:
            return False 
    return True
```

### Other variants
```python
def valid_parentheses(x):
    while "()" in x:
        x = x.replace("()", "")
    return x == ""
```
Гениально - он прото проверяет на () и удаляет их из списка. Если останутся
лишнии то скобки не правильные.

```python
def valid_parentheses(s:str):
    lvl = 0
    for c in s:
        lvl += (c=='(') - (c==')')
        if lvl<0: return False
    return not lvl
```
В данном случае кажду итерацию сначала lvl должен получить какое-то количество
положительных балов, т.к. True эквивалент 1. Если идет не правильная скобка
lvl уходит в минус и проверка прекращается и передается False.

## Divide and Conquer

### Instruction
Given a mixed array of number and string representations of integers, add up the non-string integers and subtract the total of the string integers.

Return as a number.
### Test
```python
def basic_test_cases():
    test.assert_equals(div_con([9, 3, '7', '3']), 2)
    test.assert_equals(div_con(['5', '0', 9, 3, 2, 1, '9', 6, 7]), 14)
    test.assert_equals(div_con(['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']), 13) 
    test.assert_equals(div_con(['1', '5', '8', 8, 9, 9, 2, '3']), 11)
    test.assert_equals(div_con([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)
```

### My variant
```python
def div_con(x):
    num = 0
    for i in x:
        num = num + i if isinstance(i, int) else num - int(i)
    return num
```

### Other variants
```python
def div_con(lst):
    return sum(n if isinstance(n, int) else -int(n) for n in lst)
```
Автор делает список положительных и отрицателных значений потом их суммирует