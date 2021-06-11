import random
import sys
from typing import Generator


symbols_parameter = {
    'latin': (97, 122),
    'cyrilic': (1072, 1105),
    'digits': (48, 57)
}


def generate_str(mysize: float, symbols: str, line: tuple, word: tuple) -> Generator:
    newsize = int(mysize * 1024 ** 2)  # in bytes
    while newsize > 0:
        words = []
        for wordss in range(0, random.randint(*line)):
            length = random.randint(*word)
            new_word = ''.join([chr(random.randint(*symbols_parameter[symbols])) for _ in range(length)])
            words.append(new_word)
        new_line = " ".join(words) + "\n"
        new_line = new_line[:newsize]
        yield new_line
        newsize -= len(new_line)
        sys.stdout.write('\r')
        status = (1 - newsize / (mysize * 1024 * 1024)) * 100
        sys.stdout.write("[%-100s] %d%%" % ('%' * int(status),   status))
        sys.stdout.flush()


def generate_file(size: float, symbols: str = 'latin', line: tuple = (10, 50), word: tuple = (5, 9)):
    with open('my generated file.txt', 'w', newline='\n') as k:
        k.writelines(generate_str(size, symbols, line, word))


if __name__ == "__main__":
    if len(sys.argv) == 1:
        h = str(input("Введите '+', если хотите ввести значения сами, или '-', если хотите оставить значения по умолчанию: "))
        if (h == "+"):
            size = int(input("Введите размер в мегабайтах выходного файла: "))
            generate_file(size, symbols='latin')
        elif (h == "-"):
            generate_file(5, symbols='latin')
        else: 
            print('Input Error')
    elif sys.argv[1] == '-s' and len(sys.argv) == 3:
        generate_file(float(sys.argv[2]))

