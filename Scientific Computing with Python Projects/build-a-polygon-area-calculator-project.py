class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, new_width):
        self.width = new_width
        return
    
    def set_height(self, new_height):
        self.height = new_height
        return

    def get_area(self):
        return (self.width * self.height)

    def get_perimeter(self):
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self):
        return ((self.width **2 + self.height**2)**0.5)

    def get_picture(self):
        if (self.width > 50 or self.height > 50):
            return 'Too big for picture.'

        lines = ['*'*self.width + '\n' for i in range(self.height)]
        return ''.join(lines)
    
    def get_amount_inside(self, figure):
        if (figure.height > self.height and figure.height > self.width) or (figure.width > self.height and figure.width > self.width):
            return 0
            
        elif figure.height <= self.height:
            height_times = self.height // figure.height
            width_times = self.width // figure.width
            return height_times*width_times

        elif figure.height <= self.width:
            height_times = self.height // figure.width
            width_times = self.width // figure.heigth
            return height_times*width_times


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        self.width = side
        self.height = side
        return 

    def set_side(self, new_side):
        self.side = new_side
        self.width = new_side
        self.height = new_side
        return

    def set_width(self, new_width):
        self.side = new_width
        self.height = new_width
        return
    
    def set_height(self, new_height):
        self.width = new_height
        self.side = new_height
        return

    def __str__(self):
        return f'Square(side={self.side})'

