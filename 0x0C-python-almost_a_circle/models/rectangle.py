#!/usr/bin/python3
"""
"""


class Base():
    """define class, non-base counter
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """init self and id
        """
        if id is not None:
            """value of base object
            """
            self.id = id
        else:
            """count num of non-base objects
            """
            Base.__nb_objects += 1
            self.id = Base.__nb_objects


class Rectangle(Base):
    """
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        """
        return self.__width

    @width.setter
    def width(self, width):
        """
        """
        if isinstance(width, int) is not True:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """
        """
        return self.__height

    @height.setter
    def height(self, height):
        """
        """
        if isinstance(height, int) is not True:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
        """
        if isinstance(x, int) is not True:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
        """
        if isinstance(y, int) is not True:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def area(self):
        return self.height * self.width

    def display(self):
        for i in range(self.y):
            print()
        for i in range(self.height):
            for h in range(self.x):
                print(" ", end="")
            for h in range(self.width):
                print("#", end="")
            if i + 1 <= self.height:
                print()

    def __str__(self):
        args = (self.id, self.x, self.y, self.width, self.height)
        return "[Rectangle] ({}) {}/{} - {}/{}".format(*args)

    def update(self, *args, **kwargs):

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]

        else:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'width':
                    self.width = v
                if k == 'height':
                    self.height = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v
