#!/usr/bin/env python3

def fizzBuzz(n,n2):
    for i in range(n, n2+1):
        if i % 3 == 0:
            print("Fizz")
    
        elif i % 5 == 0:
            print("Buzz")
            
        elif i % 15 == 0:
            print("FizzBuzz")
            
        else:
            print(i)

fizzBuzz(1,100)
