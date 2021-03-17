"""19. Write a Python class to find validity of a string of parentheses, '(', ')',
'{', '}', '[' and ']. These brackets must be close in the correct order, for
example "()" and "()[]{}" are valid but "[)", "({[)]" and "{{{" are invalid"""




class validity:

    @staticmethod
    def is_valid(str1):
        lst, dict1 = [], {"(": ")", "{": "}", "[": "]"}
        for p in str1:
            if p in dict1:
                lst.append(p)
            elif len(lst) == 0 or dict1[lst.pop()] is not p:
                return False
        return len(lst) == 0


print(validity().is_valid("()"))
print((validity().is_valid("[)")))
print((validity().is_valid("{{{")))
print((validity().is_valid("{{{}}}[]()")))



















































# class python_:
#    def valid_parenthese(self, str1):
#         lst, di = [], {"(": ")", "{": "}", "[": "]"}
#         for parenthese in str1:
#             if parenthese in di:
#                 lst.append(parenthese)
#             elif len(lst) == 0 or di[lst.pop()] != parenthese:
#                 return False
#         return len(lst) == 0
#
# print(python_().valid_parenthese("(){}[]"))
# print(python_().valid_parenthese("()[{)}"))