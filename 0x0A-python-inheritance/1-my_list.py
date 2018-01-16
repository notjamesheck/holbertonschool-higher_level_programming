#!/usr/bin/python3
"""class that inherits from list
"""

class MyList(list):
    """class list
    """
    def print_sorted(self):
        """prints the list sorted
        """
        print(sorted(self))
