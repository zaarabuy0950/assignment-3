"""17. Write a program that serves as a basic calculator. It asks for two
numbers, then it asks for an operator. Gracefully deal with input that
doesn't cleanly convert to numbers. Deal with division by zero errors."""



def calculator(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    else:
        try:
            return num1 / num2
        except ZeroDivisionError:
            return "Divide by 0 Error"


n1 = int(input("Enter a number: "))
n2 = int(input("Enter another number: "))
operator = input("Enter a operator: ")
print(calculator(n1, n2, operator))






































#
# def calc(num1, num2, operator):
#     if (operator == "+"):
#         print(num1 + num2)
#
#     if (operator == "-"):
#         print(num1 - num2)
#
#     if (operator == "*"):
#         print(num1 * num2)
#
#     if (operator == "/"):
#         if (num2 != 0):
#             print(num1 / num2)
#         else:
#             print("Division by zero not applicable")
#
#
# num1 = input("Enter the first number:")
# num2 = input(" Enter the second number:")
# operator = input(" Enter the operator:")
#
# num1 = float(num1)
# num2 = float(num2)
#
# if operator == "/" or operator == "*" or operator == "+" or operator == "-":
#     calc(num1, num2, operator)
#
# else:
#     print(" Invalid operator")