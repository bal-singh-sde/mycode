#!/usr/bin/env python3

goblins_file = open("/home/student/mycode/challenges/puzzle1.txt", "r")
numbers = []
answer = 0.0
answer2 = 0.0
for line in goblins_file:
    line = int(line.strip("\n"))
    numbers.append(line)

def multiplyNumbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            if numbers[i]+numbers[j] == 2020:
                answer = numbers[i]*numbers[j]
    return answer

def multiplyThreeNumbers(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)-1):
            for k in range(len(numbers)-2):
                if numbers[i]+numbers[j]+numbers[k] == 2020:
                    answer2 =  numbers[i]*numbers[j]*numbers[k]
    return answer2

print("Two Numbers", multiplyNumbers(numbers))
print("Three Numbers", multiplyThreeNumbers(numbers))
