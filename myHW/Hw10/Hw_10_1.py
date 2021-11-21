import argparse
from multiprocessing import Pool

def factorize(n):
    possible_divider = 2
    dividers = []
    while n != 1:
        while n % possible_divider == 0:
            n //= possible_divider
            dividers.append(possible_divider)
        possible_divider += 1
    return dividers

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("integers", type=int, nargs='*')
    numbers = vars(parser.parse_args())['integers']

    with Pool() as p:
        factorized = p.map(factorize, numbers)

    for pair in zip(numbers, factorized):
        print(f"{pair[0]}:", *pair[1])
