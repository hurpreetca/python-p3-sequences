#!/usr/bin/env python3


def print_fibonacci(length):
    first_number = 0
    second_number = 1
    fib = []
    for i in range(length):
        fib.append(first_number)
        first_number, second_number = second_number, first_number + second_number

    print(fib)


print_fibonacci(10)
