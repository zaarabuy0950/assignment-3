#12. Create a function, is_palindrome, to determine if a supplied word is the same if the letters are reversed.

asd = input("enter a string:")
qwe = asd[::-1]
print(qwe)
def is_palindrome(asd, qwe):
    if asd == qwe:

        return f"The Word are Same string"
    else:
        return f"The word are not same string"

print(is_palindrome(asd,qwe))

