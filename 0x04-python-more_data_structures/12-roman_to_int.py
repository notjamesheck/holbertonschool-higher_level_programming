#!/usr/bin/python3
def roman_to_int(roman_string):
    if isinstance(roman_string, str):
        rom = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500}
        rom_string = list(roman_string)
        summ = 0
        currennt = 0
        nextt = 0
        for i in range(0, len(rom_string)-1):
            currennt = rom[rom_string[i]]
            nextt = rom[rom_string[i + 1]]
            if currennt < nextt:
                summ -= currennt
            else:
                summ += currennt
        summ += rom[rom_string[-1]]
        return summ

if __name__ == "__main__":
    rom_num = "XCIX"
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
