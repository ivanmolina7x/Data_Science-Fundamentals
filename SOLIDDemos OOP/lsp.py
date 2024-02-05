class Shape:
    def __init__(self):
        self._width = 0
        self._height = 0

    def get_width(self):
        return self._width
    def set_width(self, value):
        self._width = value

    def get_height(self):
        return self._height
    def set_height(self, value):
        self._height = value

    width = property(get_width, set_width)
    height = property(get_height, set_height)

class Rectangle(Shape):
    pass

class Square(Shape):
    def get_width(self):
        return self._width
    def set_width(self,value):
        if( (value != self._height) and (self._width != 0)):
            raise Exception("Width and Height for Square cant be different")
        else:
            self._width = value
            self._height = value

    def get_height(self):
        return self._height
    def set_height(self, value):
        if((value != self._width) and (self._height != 0)) :
            raise Exception("Width and Height for Square cant be different")
        else:
            self._height = value
            self._width = value
        
    width = property(get_width, set_width)
    height = property(get_height, set_height)

from typing import List
class AreaCalculator:
    def calculateArea( self, shapes: List[Shape]):
        for shape in shapes:
            print(f'Area : {shape.width * shape.height}')

# class Line:
#     def __init__(self,length):
#         self.length = length

class Box:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
square = Square()
square.height = 10

rectangle = Rectangle()
rectangle.width = 10
rectangle.height = 5

#line = Line(10)
box = Box(10,20)

shapes = [square, rectangle, box]
AreaCalculator().calculateArea(shapes)
