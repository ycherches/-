import sys


def fib(n: int) -> int:
	elemf, elems, seq = 0, 1, [0]
	for i in range(n):
		elemf, elems = elems, elemf + elems
		seq.append(elems)
	return seq[n]


if __name__ == '__main__':
	if len(sys.argv) > 1:
		n = sys.argv[1]
	else: 
		n = input("Введите номер числа Фибоначи: ")

	if n.isdigit():
		n = int(n)
		print(fib(n))
	else:
		print('Input Error')

