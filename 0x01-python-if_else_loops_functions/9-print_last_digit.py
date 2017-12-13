#/usr/bin/python3
def print_last_digit(number):
    num = number
    if num < 0:
        num = abs(num) % 10
    else:
        num = num % 10
    print("{}".format(num), end='')
    return num
