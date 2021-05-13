#!/usr/bin/env python3

def main(size):
    for i in range(size):
        for j in range(i):
            print('*',end='')
        print('*')
    for i in range(size):
        for j in range(size -i):
            print('*', end='')
        print('*')


main(5)
