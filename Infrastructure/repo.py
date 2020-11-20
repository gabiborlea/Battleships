class Repository:
    def __init__(self):
        self._data = [[' ']*8, [' ']*8, [' ']*8, [' ']*8, [' ']*8, [' ']*8, [' ']*8, [' ']*8]
        
    def get_data(self):
        return self._data
    
    def add_ship(self, ship):
        
        if ship.get_direction() == 1:
            x = ship.get_x()
            y = ship.get_y()
            if y - ship.get_size() + 1 < 0:
                raise RepoError("invalid position")
            for i in range(y, y - ship.get_size(), -1):
                if self._data[i][x] != ' ':
                    raise RepoError("there is a ship!")
            
            for i in range(y, y - ship.get_size(), -1):
                self._data[i][x] = ship.get_ship_id()
                
                
        if ship.get_direction() == -1:
            x = ship.get_x()
            y = ship.get_y()
            if x - ship.get_size() + 1 < 0:
                raise RepoError("invalid position")
            for i in range(x, x - ship.get_size(), -1):
                if self._data[y][i] != ' ':
                    raise RepoError("there is a ship!")
            
            for i in range(x, x - ship.get_size(), -1):
                self._data[y][i] = ship.get_ship_id()
                
    def add_miss_hit(self, x, y, c):
        if self._data[y][x] not in ['M', 'H']:
            self._data[y][x] = c
        else:
            raise RepoError("box already hit")
        
    def get_min_col(self):
        nr = 0
        mn = 0
        min_column = 0
        for i in range(8):
            nr = 0
            for j in range(8):
                if self._data[j][i] != 'M' and self._data[j][i] != 'H':
                    nr += 1
            if nr > mn:
                mn = nr 
                min_column = i 
                
        return  min_column
        
    def get_cood_info(self, x, y):
        return self._data[y][x]
            
class RepoError(Exception):
    pass
