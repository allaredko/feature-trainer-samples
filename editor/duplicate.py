import math


def demo(a, b, c):
    return_type_of_sqrt = math.sqrt(b ** 2 - 4 * a * c)
    root1 = (-b + return_type_of_sqrt) / (2 * a)
    root2 = (-b - return_type_of_sqrt) / (2 * a)
    print(root1, root2)