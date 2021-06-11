class test():
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def first_variant(obj, value):
    attributes = obj.__dict__
    k = 0
    for elem in attributes:
        if attributes[elem] == value:
            k = elem
    if k != 0:
        return k
    else:
        return "Отсутсвует"


def second_variant(obj, value):
    for elem in dir(obj):
        if getattr(obj, elem) == value:
            return elem
    return "Отсутсвует"


if __name__ == '__main__':
    x = test(33, 58, 99)
    print(first_variant(x, 33))
    print(second_variant(x, 33))
    x.d = 67
    print(first_variant(x, 67))
    print(second_variant(x, 67))
