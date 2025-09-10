def basic_op(operator, value1, value2):
    match operator:
        case i if i == "+":
            return value1 + value2
        case i if i == "-":
            return value1 - value2
        case i if i == "*":
            return value1 * value2
        case _:
            return value1 / value2