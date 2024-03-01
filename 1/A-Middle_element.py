'''
Рассмотрим три числа aa, bb и cc. Упорядочим их по возрастанию.
Какое число будет стоять между двумя другими?

Формат ввода
В единственной строке записаны три целых числа a, b, c (−1000≤a,b,c≤1000−1000≤a,b,c≤1000),
числа разделены одиночными пробелами.

Формат вывода
Выведите число, которое будет стоять между двумя другими после упорядочивания.
'''


def middle_element(a, b, c):
    if a <= b <= c or c <= b <= a:
        return b
    elif b <= a <= c or c <= a <= b:
        return a
    else:
        return c


def main():
    a, b, c = map(int, input().split())
    print(middle_element(a, b, c))


if __name__ == '__main__':
    main()