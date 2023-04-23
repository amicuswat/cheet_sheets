import time


def get_nod(a: int, b: int) -> int:
    """Вычисляем нод для двух натуральных чисел a и b
        по алгоритму Эвклида

    :param a: первое натуральное число
    :param b: второе натуральное число
    :return: nod
    """
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a

    return a


def test_nod(func):
    # записал эту функцию чтобы потренироваться в синтаксисе

    # * ----- test 1 ----- *
    a = 28
    b = 35
    res = func(a, b)
    if res == 7:
        print('test 1 - ok')
    else:
        print('test 1 - fail')

    # * ----- test 2 ----- *
    a = 2
    b = 10000000
    st = time.time()
    res = func(a, b)
    et = time.time()
    dt = et - st
    if res == 2 and dt < 1:
        print('test 2 - ok')
    else:
        print('test 2 - fail')

test_nod(get_nod)  # передаем просто ссылку на функцию без ее запуска
