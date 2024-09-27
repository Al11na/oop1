#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Task1:
    def __init__(self, first, second):
        # Проверка корректности аргументов
        if not (isinstance(first, int) and isinstance(second, int)):
            raise ValueError("Числитель и знаменатель должны быть целыми числами.")
        if first <= 0 or second <= 0:
            raise ValueError("Числитель и знаменатель должны быть положительными.")
        if second == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю.")

        self.first = first  # числитель
        self.second = second  # знаменатель

    def ipart(self):
        # Выделение целой части дроби (first // second)
        if self.second == 0:
            raise ZeroDivisionError("Знаменатель не может быть равен нулю.")
        return self.first // self.second

    @classmethod
    def read(cls):
        try:
            first = int(input("Введите числитель (целое положительное число): "))
            second = int(input("Введите знаменатель (целое положительное число): "))
            return cls(first, second)
        except ValueError as e:
            print(f"Ошибка ввода: {e}")
        except ZeroDivisionError as e:
            print(f"Ошибка: {e}")

    def display(self):
        print(f"Дробь: {self.first}/{self.second}")


def make_fraction(first, second):
    try:
        return Task1(first, second)
    except (ValueError, ZeroDivisionError) as e:
        print(f"Ошибка создания структуры: {e}")
        return None


if __name__ == '__main__':
    # Демонстрация возможностей класса
    f = Task1.read()
    if f:
        f.display()
        print(f"Целая часть дроби: {f.ipart()}")

    # Пример использования функции make_fraction с вводом пользовательских данных
    try:
        first = int(input("Введите числитель для второй дроби (целое положительное число): "))
        second = int(input("Введите знаменатель для второй дроби (целое положительное число): "))
        f2 = make_fraction(first, second)
        if f2:
            f2.display()
            print(f"Целая часть дроби: {f2.ipart()}")
    except ValueError as e:
        print(f"Ошибка ввода: {e}")
    except ZeroDivisionError as e:
        print(f"Ошибка: {e}")
