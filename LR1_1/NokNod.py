def nod(A: int, B: int) -> int:
    if B > A:
        B, A = A, B
    while B != 0:
        A, B = B, A % B
    return A


def nok(A: int, B: int) -> int:
    return A * B // nod(A, B)


if __name__ == '__main__':
    A, B = input("Введите два натуральных числа ").split()

    if A.isdigit() and B.isdigit() and A != '0' and B != '0':
        A, B = int(A), int(B)
        print(nod(A, B), nok(A, B))
    else:
        print('Input Error')

