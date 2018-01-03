#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    i = 0
    arr = []
    while i < list_length:
        try:
            arr.append(my_list_1[i] / my_list_2[i])
        except (ValueError, TypeError):
            print("wrong type")
            arr.append(0)
        except IndexError:
            print("out of range")
            arr.append(0)
        except ZeroDivisionError:
            print("division by 0")
            arr.append(0)
        finally:
            i += 1
    return arr
