#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        self.size = size
        super().__init__(size, size, x, y, id)

    def __str__(self):
        args = (self.id, self.x, self.y, self.size)
        return "[Square] ({}) {}/{} - {}".format(*args)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        if isinstance(size, int) is not True:
            raise TypeError("width must be an integer")
        if size <= 0:
            raise ValueError("width must be > 0")
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):

        if args:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.size = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]

        elif kwargs:
            for k, v in kwargs.items():
                if k == 'id':
                    self.id = v
                if k == 'size':
                    self.size = v
                if k == 'x':
                    self.x = v
                if k == 'y':
                    self.y = v

    def to_dictionary(self):
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
