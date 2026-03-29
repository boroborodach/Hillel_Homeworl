def difference(*args):
    """
    Calculates the difference between the maximum and minimum values in the provided arguments.

    The result is rounded to two decimal places. If no arguments are provided,
    the function returns 0.

    :param args: A variable number of numeric values (integers or floats).
    :type args: float | int
    :return: The difference between the largest and smallest numbers, or 0 if empty.
    :rtype: float | int
    """
    if len(args) == 0:
        return 0
    return round(max(args) - min(args), 2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
