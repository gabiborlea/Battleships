class Ship:
    def __init__(self, size, x, y, direction):
        self._size = size
        self._x = x
        self._y = y
        self._direction = direction

    def get_size(self):
        return self.__size


    def get_x(self):
        return self.__x


    def get_y(self):
        return self.__y


    def get_direction(self):
        return self.__direction


    def set_size(self, value):
        self.__size = value


    def set_x(self, value):
        self.__x = value


    def set_y(self, value):
        self.__y = value


    def set_direction(self, value):
        self.__direction = value
        
    def destroy(self):
        self._size -= 1

    _size = property(get_size, set_size, None, None)
    _x = property(get_x, set_x, None, None)
    _y = property(get_y, set_y, None, None)
    _direction = property(get_direction, set_direction, None, None)
        
    


class Battleship(Ship):
    def __init__(self, x, y, direction):
        super().__init__(4, x, y, direction)
        
    def get_ship_id(self):
        return 'B'
    
class Cruiser(Ship):
    def __init__(self, x, y , direction):
        super().__init__(3, x, y, direction)
        
    def get_ship_id(self):
        return 'C'
    
class Destoryer(Ship):
    def __init__(self, x, y, direction):
        super().__init__(2, x, y, direction)
        
    def get_ship_id(self):
        return 'D'
        

