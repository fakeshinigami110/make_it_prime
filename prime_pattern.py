import sys
import numpy as np
from sympy import isprime
from colorama import init, Fore, Back, Style
from collections import Counter
sys.setrecursionlimit(5000)
np.set_printoptions(threshold=np.inf)

def make_prime(pattern):
    matrix = np.array([list(line.strip()) for line in pattern.split('\n') if line.strip()], dtype=int)
    rows, cols = matrix.shape

    def to_number(m):
        return int(''.join(m.flatten().astype(str)))

    def check_and_return(m):
        if isprime(to_number(m)):
            return m
        return None

    num = to_number(matrix)
    if isprime(num):
        return matrix

    last_row = rows - 1
    for last_col in range(cols - 1, -1, -1):
        original_digit = matrix[last_row, last_col]
        for digit in range(10):
            if digit == original_digit:
                continue
            temp = matrix.copy()
            temp[last_row, last_col] = digit
            result = check_and_return(temp)
            if result is not None:
                return result

    first_row = 0
    for first_col in range(cols):
        original_digit = matrix[first_row, first_col]
        for digit in range(10):
            if digit == original_digit:
                continue
            temp = matrix.copy()
            temp[first_row, first_col] = digit
            result = check_and_return(temp)
            if result is not None:
                return result

    last_row = rows - 1
    for last_col1 in range(cols - 1, -1, -1):
        for last_col2 in range(last_col1 - 1, -1, -1):
            original_digit1 = matrix[last_row, last_col1]
            original_digit2 = matrix[last_row, last_col2]

            for digit1 in range(10):
                if digit1 == original_digit1:
                    continue
                for digit2 in range(10):
                    if digit2 == original_digit2:
                        continue
                    temp = matrix.copy()
                    temp[last_row, last_col1] = digit1
                    temp[last_row, last_col2] = digit2
                    result = check_and_return(temp)
                    if result is not None:
                        return result

    first_row = 0
    last_row = rows - 1
    for first_col in range(cols):
        original_first_digit = matrix[first_row, first_col]
        for last_col in range(cols):
            original_last_digit = matrix[last_row, last_col]

            for digit1 in range(10):
                if digit1 == original_first_digit:
                    continue
                for digit2 in range(10):
                    if digit2 == original_last_digit:
                        continue
                    temp = matrix.copy()
                    temp[first_row, first_col] = digit1
                    temp[last_row, last_col] = digit2
                    result = check_and_return(temp)
                    if result is not None:
                        return result

    for first_col1 in range(cols):
        for first_col2 in range(first_col1 + 1, cols):
            original_digit1 = matrix[first_row, first_col1]
            original_digit2 = matrix[first_row, first_col2]

            for digit1 in range(10):
                if digit1 == original_digit1:
                    continue
                for digit2 in range(10):
                    if digit2 == original_digit2:
                        continue
                    temp = matrix.copy()
                    temp[first_row, first_col1] = digit1
                    temp[first_row, first_col2] = digit2
                    result = check_and_return(temp)
                    if result is not None:
                        return result

    return "no prime found with given constraints"





init()


def introduce():
    x = r"""
         ____  _     _       _                       _     _ _  ___  
        / ___|| |__ (_)_ __ (_) __ _  __ _ _ __ ___ (_)   / / |/ _ \ 
        \___ \| '_ \| | '_ \| |/ _` |/ _` | '_ ` _ \| |   | | | | | |
         ___) | | | | | | | | | (_| | (_| | | | | | | |   | | | |_| |
        |____/|_| |_|_|_| |_|_|\__, |\__,_|_| |_| |_|_____|_|_|\___/ 
                               |___/                 |_____|         
    """
    line = "______________________________________________________________________________________________"


    print(Fore.RED + line)
    print(Style.RESET_ALL)
    print(x)
    print(Fore.RED + line)
    print(Fore.GREEN+'telegram : @shinigami_110 ')
    print(Style.RESET_ALL , end='')
    text = """
This project converts numeric patterns
into prime numbers by intelligently modifying digits with minimal changes.:    """
    print(text)

    print("Exit [0]")
    print("Generate new pattern template [1]")
    print("Convert existing pattern to prime [2]")

def get_char():
    if sys.platform == 'win32':
        import msvcrt
        return msvcrt.getch().decode('utf-8')
    else:
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch
def detect_pattern_char(text):
    """Find the most frequent character (pattern) in the input text"""
    from collections import Counter
    chars = [c for c in text if c not in {'\n', ' ', '\t'}]
    if not chars:
        return '0'
    return Counter(chars).most_common(1)[0][0]

def color_highlighted_output(matrix, pattern_char):
    """Print matrix with pattern characters colored red"""
    for row in matrix:
        for num in row:
            if str(num) == pattern_char:
                print(f"{Fore.RED}{num}{Style.RESET_ALL}", end="")
            else:
                print(num, end="")
        print()

def main():
    introduce()
    while True:
        char = get_char()
        if char.isdigit():
            number = int(char)
            if number == 0:
                print("\nExiting...")
                break
            elif number == 1:
                inp = input("please enter your template's rows columns numbers and the digit you want to fill like : row clos digit for example  20 20 1 :")
                try:
                    parts = inp.split()
                    if len(parts) != 3:
                        print("please enter exactly 3 numbers")
                        continue

                    rows, columns, num = map(int, parts)
                    template = np.full((rows, columns), num)

                    print("\nhere is your matrix:\n")
                    for row in template:
                        print(' '.join(map(str, row)))

                except ValueError:
                    print("invalid numbers")
                except Exception as e:
                    print(f"error {e}")


            elif number == 2:

                print("Paste your pattern (press Enter twice after pasting):")
                lines = []
                while True:
                    line = input()
                    if not line:

                        if lines:
                            break
                        continue
                    lines.append(line)
                original_matrix = np.array([list(line) for line in lines])

                original_text = '\n'.join(lines)

                print('\nPrime number result:')

                result = make_prime(original_text)

                if isinstance(result, np.ndarray):
                    original_matrix = original_matrix.astype(str)
                    result_matrix = result.astype(str)
                    pattern_char = detect_pattern_char(original_text)
                    for i in range(result.shape[0]):  # rows
                        for j in range(result.shape[1]):  # columns
                            current_char = result_matrix[i, j]
                            original_char = original_matrix[i, j]
                            if original_char == pattern_char or original_char != current_char:
                                print(f"{Fore.RED}{current_char}{Style.RESET_ALL}", end="")
                            else:
                                print(current_char, end="")

                        print()
                else:
                    print(result)
            text2 = """
This script make your pattern prime if possible 
                """
            line = "\n______________________________________________________________________________________________"

            print(Fore.BLUE + line)
            print(Style.RESET_ALL)
            print(text2)

            print("Exit [0]")
            print("get template [1]")
            print("send your template [2]")


if __name__ == "__main__":
    main()