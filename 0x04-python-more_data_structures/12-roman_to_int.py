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
    else:
        return 0

if __name__ == "__main__":
    rom_num = "I"
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
    rom_num = "III"
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
    rom_num = "XXI"
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
    rom_num = "IV"
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
    rom_num = "CXXIV"
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
    rom_num = 657624
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
    rom_num = None
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
    rom_num = "XCIX"
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
    rom_num = "LXXXIX"
    print("{} = {}".format(rom_num, roman_to_int(rom_num)))
