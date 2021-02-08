#!/bin/python3

def is_weird(input):

    input = convert_input(input)
    if input%2 != 0:
        weird_message(input)
    elif input %2 ==0 and 1 < input < 6:
        not_weird_message(input)
    elif input %2 ==0 and 5 < input < 21:
        weird_message(input)
    else:
        not_weird_message(input)

def weird_message(input):
    print(f'{input} is weirdooo!!!')
    
def not_weird_message(input):
    print(f'{input} is not weird!')

def convert_input(input):
    return abs(input)

if __name__ == '__main__':

    is_weird(int(input("Enter n:\n").strip()))