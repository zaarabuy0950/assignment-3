"""8. Write a function, is_prime, that takes an integer and returns True if the
number is prime and False if the number is not prime."""


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    else:
        for i in range(2, number):
            if number % i == 0 and number != i:
                return False
    return True


result = int(input("enter a number:"))
print(is_prime(result))
