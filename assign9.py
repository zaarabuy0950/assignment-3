"""9. Write a binary search function. It should take a sorted sequence and
the item it is looking for. It should return the index of the item if found.
It should return -1 if the item is not found."""


def binaray_search(arry, item):
    for i in range(len(arry)):
        if item in arry:
            return arry.index(item)
        else:
            return -1


arr_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
abj = int(input("Enter the number:"))
print(binaray_search(arr_list, abj))
