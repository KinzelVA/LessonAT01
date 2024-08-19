def modulo(dividend, divisor):
    """Возвращает остаток от деления dividend на divisor.

    Если divisor равен нулю, вызывает исключение ZeroDivisionError.
    """
    if divisor == 0:
        raise ZeroDivisionError("Деление на ноль невозможно")
    return dividend % divisor
