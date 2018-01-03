#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    arr = []
    print("this is the starting array: {}".format(arr))
    print("here is the list length: {}".format(list_length))
    while i < list_length:
        print("i is: {}".format(i))
        try:
            arr.append(my_list_1[i] / my_list_2[i])
            print("it worked: {}".format(arr))
        except (ValueError, TypeError):
            print("wrong type")
            arr.append(0)
        except IndexError:
            print("out of range")
            arr.append(0)
        except ZeroDivisionError:
            print("division by zero")
            arr.append(0)
        finally:
            i += 1
    return arr
