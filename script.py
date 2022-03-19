import sys
import argparse
import numpy as np
import random


def generateRandomString(n):
    arr = np.random.randint(2, size=(n,))
    return arr


def generateDeletedStrings(string, q, m, n):
    deletedStrings = np.zeros((m, n))
    positionAtString = 0
    for i in range(m):
        positionAtString = 0
        for j in range(n):
            if random.random() >= q:
                deletedStrings[i][positionAtString] = string[j]
                positionAtString += 1
        while positionAtString < n:
            deletedStrings[i][positionAtString] = 2
            positionAtString += 1
    return deletedStrings


def bitwiseMajorityAlignment(deletedStrings, m, n):
    c = np.zeros(m, dtype=np.int8)
    t = np.zeros(n)
    for i in range(n):
        numberZeros = 0
        numberOnes = 0
        for j in range(m):
            if deletedStrings[j][c[j]] == 0:
                numberZeros += 1
            if deletedStrings[j][c[j]] == 1:
                numberOnes += 1
        if numberOnes >= numberZeros:
            t[i] = 1
        else:
            t[i] = 0
        for j in range(m):
            if deletedStrings[j][c[j]] == t[i]:
                c[j] += 1
    return t


def simulate(q, t, n, m):
    successful = 0
    not_successful = 0
    for i in range(t):
        string = generateRandomString(n)
        error_strings = generateDeletedStrings(string, q, m, n)
        reconstructed_string = bitwiseMajorityAlignment(error_strings, m, n)
        print("String #{}".format(i+1))
        print(string)
        print("Generated error strings:")
        print(error_strings)
        print("Reconstructed string #{}:".format(i+1))
        print(reconstructed_string)
        print("Is reconstructed string = original string?")
        print(np.array_equal(string, reconstructed_string))
        print()
        if np.array_equal(string, reconstructed_string):
            successful += 1
        else:
            not_successful += 1
    print("Total number of successful strings: {}".format(successful))
    print("Total number of unsuccessful strings: {}".format(not_successful))


def main(args=sys.argv[1:]):
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--q", help="Probability of Deletion", type=float, default=None)
    parser.add_argument("--trials",
                        help="Used for testing",
                        type=int,
                        default=None)
    parser.add_argument("--n", help="Length of string",
                        type=int, default=None)
    parser.add_argument(
        "--m", help="Number of deleted strings", type=int, default=None)

    args = parser.parse_args()
    t = args.trials
    m = args.m
    n = args.n
    q = args.q
    simulate(q, t, m, n)


if __name__ == '__main__':
    main()
