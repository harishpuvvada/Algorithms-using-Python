import sys

def solution(lis):

    first = second = third = -sys.maxsize

    for num in lis:

        if num > first:

            second = first

            third = second

            first = num

        elif num > second :

            third = second

            second = num


        elif num > third :

            third = num

    print(first, second, third)


    return first * second * third
