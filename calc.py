# -*- coding:utf-8 -*-


def addition(a, b):
    c = a + b
    return c


def subtraction(a, b):
    c = a - b
    return c


def multiplication(a, b):
    c = a * b
    return c


def division(a, b):
    c = a / b
    """
    try:
        c = a / b
    except ZeroDivisionError as e:
        c = 99999
    except Exception as e:
        c = 99999
    """
    return c
