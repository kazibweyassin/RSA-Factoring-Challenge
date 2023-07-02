import sys


def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append((i, n))
    if n > 1:
        factors.append((n, 1))
    return factors


def factorize_file(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            number = int(line.strip())
            factors = factorize(number)
            for factor in factors:
                outfile.write(f"{number}={factor[0]}*{factor[1]}\n")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: factors <file>")
        sys.exit(1)
    input_file = sys.argv[1]
    output_file = "factorizations.txt"
    factorize_file(input_file, output_file)
