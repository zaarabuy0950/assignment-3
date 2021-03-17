""""20. Write a Python class to find the three elements that sum to zero from
a list of n real numbers.
Input array : [-25, -10, -7, -3, 2, 4, 8, 10]
Output : [[-10, 2, 8], [-7, -3, 10]]"""


class from_Zero:

    def my_func(self, my_list):
        list1 = []
        lastone = []
        for i in range(0, len(my_list)-2):
            for j in range(i+1, len(my_list)-1):
                for k in range(j+1, len(my_list)):
                    if my_list[i] + my_list[j] + my_list[k] == 0:
                        list1 = [my_list[i], my_list[j], my_list[k]]
                        lastone.append(list1)
        print(lastone)


C1 = from_Zero()
C1.my_func([-25, -10, -7, -3, 2, 4, 8, 10])