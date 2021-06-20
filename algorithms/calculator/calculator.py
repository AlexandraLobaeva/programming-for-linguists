"""
Programming for linguists

Implementation of the Reverse Polish Notation Converter
"""
from algorithms.calculator.reverse_polish_notation import ReversePolishNotation
from data_structures.stack.stack import Stack


class ReversePolishNotationCalculator:
    """
    Calculator of expression in Reverse Polish Notation
    """
    def __init__(self):
        self.stack = Stack()

    def calculate(self, rpn_expression: ReversePolishNotation) -> float:
        """
        Main method of the ReversePolishNotationCalculator class.
        Calculating result of expression in Reverse Polish Notation.

        :param rpn_expression: expression in Reverse Polish Notation Format
        :return: result of the expression
        """
                for el in rpn_expression:
            if isinstance(el, Digit):
                self.stack.push(el)
                continue
            begin = self.stack.top()
            self.stack.pop()
            end = self.stack.top()
            self.stack.pop()
            result = el(begin, end)
            self.stack.push(result)
        res = self.stack.top()
        self.stack.pop()
        return res

    print(ReversePolishNotationCalculator().calculate(ReversePolishNotationConverter().convert('2*(2+2)')))
