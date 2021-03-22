def Nod(A, B: int) -> int:
    if B>A:
        B, A = A, B
    while B!=0:
        nod = B
        q = A % B
        A = B
        B = q
    return nod

def Nok(A, B: int) -> int:
    return (A * B // Nod(A, B))


if __name__ == '__main__':
    A, B = input().split(' ')

    if A.isdigit() and B.isdigit() and A!='0' and B!='0':
        A = int(A)
        B = int(B)
        print(Nod(A,B),Nok(A,B))
    else:
        print('Input Error')