""" This program involves two functions, test cases for each function, and
a main function which prompts the user for an expression, evaluates the
expression, and returns an appropriate result. At this point, the only
operators that will be evaluated are + and -. """

import unittest

def expression_evaluator(s):
    """ This function evaluates an expression by adding or subtracting
    user-entered integers based on the operator entered. The only two
    operators that may be applied are + and -. The appropriate syntax is
    <operator> <expression> <expression>. """
    total = 0
    temp_list = list()
    for item in s.split():
        temp_list.append(item)
    
    if temp_list[0] == "+" or temp_list[0] == "-":
        for item in temp_list:
            if item == "+":
                operator = "+"
            elif item == "-":
                operator = "-"
            else:
                try:
                    converted_int = int(item)
                except:
                    raise ValueError("An error has occured. This function only takes +, -, or integers as expressions.")
                if operator == "+":
                    total += converted_int
                elif operator == "-":
                    total -= converted_int
        return total
    else:
        raise Exception ("Your expression is invalid! You must enter an appropriate operator first!")


def main():
    """ This function prompts the user for an expression, evaluates the function
    by calling the expression_evaluator(s) function, and returns the result. """
    print("Welcome to the Expression Evaluator!")
    while True:
        try:
            exp = input("Please enter an expression to be evaluated. The appropriate syntax is <operator> <expression> <expression>.\n")
            if exp[0] == "+" or exp[0] == "-":
                break
        except Exception:
            print("Your expression is invalid! You must enter an appropriate operator first!\n Please try again!")
    result = expression_evaluator(exp)
    print("The result of your expression is", result)


class ExpressionEvaluatorTest(unittest.TestCase):
    """ Test to verify that the expression_evaluator(s) function returns the
    correct answer. """
    def test_expression_evaluator(self):
        self.assertEqual(expression_evaluator("+ 1 + 2 3"), 6)
        self.assertEqual(expression_evaluator("- 1 + 2 3"), 4)
    def test_raise_error(self):
        with self.assertRaises(Exception):
            expression_evaluator("1 + 2 3")


if __name__ == '__main__':
    # Note there is no main() This program contains only test cases.
    unittest.main(exit=False, verbosity=2)