from sys import argv, stderr
import message
from random import randint


def main():
    hq9p = HQ9Plus(args=argv)
    exit(hq9p.accumulator)


class HQ9Plus:
    accumulator: int = 0
    __source: str
    __file_name: str

    def __init__(self, args):
        if len(args) < 2:
            print(message.usage_message)
            exit(0)
        self.__file_name = args[1]
        self.__file_load(args[1])
        self.__interpreter()

    def __file_load(self, path):
        with open(file=path, mode="r", encoding="UTF-8") as f:
            self.__source = f.read()

    def __interpreter(self):
        now_line: int = 1
        now_char: int = 1
        for char in self.__source:
            if char == "H":
                self.__hello()
            elif char == "Q":
                self.__quine()
            elif char == "9":
                self.__ninety_nine_bottles_of_beer()
            elif char == "+":
                self.__increment()
            elif char == " " or char == "\t":
                pass
            elif char == "\n":
                now_line += 1
                now_char = 1
                continue
            else:
                self.__error(line=now_line, char=now_char)
            now_char += 1

    @staticmethod
    def __hello():
        print("Hello, world!", end="")

    def __quine(self):
        print(self.__source, end="")

    @staticmethod
    def __ninety_nine_bottles_of_beer():
        for i in range(99, 1, -1):
            print(f"{i} bottles of beer on the wall, {i} bottles of beer.\n"
                  f"Take one down and pass it around, {i - 1} bottles of beer on the wall.", end="")
        print("1 bottle of beer on the wall, 1 bottle of beer.\n"
              "Take one down and pass it around, no more bottles of beer on the wall.\n"
              "1 bottle of beer on the wall, 1 bottle of beer.\n"
              "Take one down and pass it around, no more bottles of beer on the wall.\n"
              "No more bottles of beer on the wall, no more bottles of beer.\n"
              "Go to the store and buy some more, 99 bottles of beer on the wall.\n", end="")

    def __increment(self):
        self.accumulator += 1

    def __error(self, line, char):
        source_list = self.__source.split("\n")
        print(f"\nfile: {self.__file_name}, line {line}")
        print(f"{source_list[line - 1]}")
        space = " " * (char - 1)
        print(f"{space}^{message.error_message[randint(0, len(message.error_message) - 1)]}", file=stderr)
        exit(-1)


if __name__ == "__main__":
    main()
