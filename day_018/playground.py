def add(*args):
    total = 0
    for n in args:
        total += n
    return total


print(add(2, 3, 667, 45, 1000))


def calculate(**kwargs):
    for keys, value in kwargs.items():
        print(keys)
        print(value)


calculate(add=3, multiply=4)
