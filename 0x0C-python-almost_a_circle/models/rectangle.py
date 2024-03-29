#!/usr/bin/python3
"""my other class Rectangle that inherits from Base"""


from models.base import Base
class Rectangle(Base):
    """Rectangle class that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """init for rectangle

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.

        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.

            """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Set and get width of the Rectangle."""

        return self.__width

    @width.setter
    def width(self, value):
        """Width_fucntion"""

        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Setand get height of the Rectangle."""

        return self.__height

    @height.setter
    def height(self, value):
        """height_fucntion"""


        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Set and get x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """set X fucntion"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Set Y fucntion"""
        """Set/get y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """ regards the y function"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculateion for area of the Rectangle"""
        return self.width * self.height

    def display(self):
        """Display for the rectangle"""

        if self.width == 0 or self.height == 0:
            print("")
            return

        for y in range(self.y):
            print()
        for i in range(self.height):
            [print(" ", end="") for x in range(self.x)]
            [print('#', end="") for j in range(self.width)]
            if i != self.height - 1:
                print("")
        print("")


    def __str__(self):
        """overriding the __str__ method"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,self.x, self.y,self.width, self.height)

    def update(self, *args, **kwargs):
        """
        latest rectangle's attributes based on provided arguments.

        Args:
            *args: A sequence of no-keyword arguments (tuples are not allowed).
                - 1st argument: id (integer)
                - 2nd argument: width (integer)
                - 3rd argument: height (integer)
                - 4th argument: x (integer)
                - 5th argument: y (integer)

        Raises:
            TypeError: If an argument is not of the expected type.
            ValueError: If an argument is not valid (e.g., negative width).
        """
        if args and len(args) !=0:
            for i, arg in enumerate(args):
                if i == 0:  # First argument for id (optional)
                    self.id = arg
                elif i == 1:  # Second argument for width (optional)
                    self.width = arg
                elif i == 2:  # Third argument for height (optional)
                    self.height = arg
                elif i == 3:  # Fourth argument for x (optional)
                    self.x = arg
                elif i == 4:  # Fifth argument for y (optional)
                    self.y = arg
        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "width":
                    self.width = value
                elif key == "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """dict_fucntion"""
        return {"id": self.id, "width": self.width, "height": self.height, "x": self.x, "y": self.y}

