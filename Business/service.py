from Domain.ships import Battleship, Cruiser, Destoryer
class Service:
    def __init__(self, ships_repo):
        self._ships_repo = ships_repo
        self._destroyed_nr = 0
        
    def add_battleship(self, x, y, direction):
        self._battleship = Battleship(x,y, direction)
        self._ships_repo.add_ship(self._battleship)
        
    def add_cruiser(self, x, y, direction):
        self._cruiser = Cruiser(x, y, direction)
        self._ships_repo.add_ship(self._cruiser)
        
    def add_destroyer(self, x, y, direction):
        self._destroyer = Destoryer(x, y, direction)
        self._ships_repo.add_ship(self._destroyer)
        
    def miss_hit(self, x, y):
        cood = self._ships_repo.get_cood_info(x,y)
        if cood == 'B':
            self._battleship.destroy() 
            self._ships_repo.add_miss_hit(x,y, 'H')
        elif cood == 'C':
            self._cruiser.destroy()
            self._ships_repo.add_miss_hit(x,y, 'H')
            
        elif cood == 'D':
            self._destroyer.destroy()
            self._ships_repo.add_miss_hit(x,y, 'H')
        else:
            self._ships_repo.add_miss_hit(x,y, 'M')
            
    def ship_distroyed(self):
        warning = ""
        if self._battleship.get_size() == 0:
            self._battleship.destroy()
            warning += "Your Battleship is destroyed"
            self._destroyed_nr += 1
            
        if self._cruiser.get_size() == 0:
            self._cruiser.destroy()
            warning += "Your Cruiser is destroyed"
            self._destroyed_nr += 1
        
        if self._destroyer.get_size() == 0:
            self._destroyer.destroy()
            warning += "Your Destroyer is destroyed"
            self._destroyed_nr += 1
            
        return warning
        
    def game_over(self):
        if self._destroyed_nr == 3:
            return True
        else:
            return False
            

class GameWarning(Exception):
    pass
