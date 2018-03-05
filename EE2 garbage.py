
""" This program involves two functions, test cases for each function, and
a main function which prompts the user for an expression, evaluates the
expression, and returns an appropriate result. At this point, the only
operators that will be evaluated are + and -. """

import unittest

def expression_evaluator(s):
    cleaned_exp = list(" ".join(s.split()))
    if cleaned_exp[0] == "+":
        operator = "+"
    elif cleaned_exp[0] == "-":
        operator = "-"
    else:
        raise Exception("You did not enter a valid operator!")
    
    numbers = list()
    for item in cleaned_exp[1:]:
        if item = "+":
            operator = "+"
        elif item = "-":
            operator = "-"
        else:
            converted_item = int(item)
            numbers.append(converted_item)

    if operator   
    

    numbers = list()
    total = 0
    if item[0] in l.split(" "):
        if item == "+":
            operator = "+"
        elif item == "-":
            operator = "-"
        else:
            raise Exception("You did not enter a valid operator!")
    for item[1:] in l.split(" "):
            converted_item = int(item)
            numbers.append(converted_item)
    if operator == "+":
        for item in numbers:
            total = numbers[0] + numbers[1]
    elif operator == "-":
        for item in numbers:
            total = numbers[0] - numbers[1]
    else:
        raise ValueError("You did not enter a valid operator!")
    return total

def main():
    print("Welcome to the Expression Evaluator!")
    exp = input("Please enter an expression to be evaluated. The appropriate syntax is <operator> <expression> <expression>.\n")
    cleaned_up_exp = " ".join(exp.split())
    result = expression_evaluator(cleaned_up_exp)
    print(result)

main()