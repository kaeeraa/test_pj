def calc(first_number: int | float = 0,
         second_number: int | float = 0,
         operator: str = '+') -> int | float:
    """
    Function to perform basic arithmetic operations.

    :param first_number: First number for the operation.
    :type first_number: int | float
    
    :param second_number: Second number for the operation.
    :type second_number: int | float
    
    :param operator: The arithmetic operation to perform (+, -, *, /).
    :type operator: str
    
    :return: The result of the arithmetic operation.
    :rtype: int | float
    """
    
    if operator == '+':
        return first_number + second_number
    elif operator == '-':
        return first_number - second_number
    elif operator == '*':
        return first_number * second_number
    elif operator == '/':
        if second_number == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return first_number / second_number
    else:
        raise ValueError("Invalid operator. Use '+', '-', '*', or '/'.")


# Newton's method for finding roots
# This function returns the approximate root of the given function within the specified tolerance
def newton_method(f, df, x0, tolerance=1e-6, ) -> float:
    """
    Newton's method for finding roots.

    This function uses Newton's method to find the approximate root of the
     given function within the specified tolerance.

    :param f: A function that represents the function whose root is to be found.
    :type f: function

    :param df: A function that represents the derivative of the function f.
    :type df: function

    :param x0: The initial guess for the root.
    :type x0: float

    :param tolerance: The tolerance level for the root finding process.
    :type tolerance: float, optional
    :default: 1e-6

    :return: The approximate root of the function f within the specified tolerance.
    :rtype: float
    """
    x = x0
    while abs(f(x)) > tolerance:
        x -= f(x) / df(x)
    return x
