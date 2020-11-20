class UI:
    def __init__(self, my_board, service, ai_board, ai, hidden):
        self._my_board = my_board
        self._ai_board = ai_board
        self._service = service
        self._ai = ai
        self._hidden = hidden
        
    def show_my_board(self):
        print(self._my_board)
    
    def show_ai_board(self):
        print(self._ai_board)
    
    def show_hidden(self):
        print(self._hidden)
        
    def place_battleship(self):
        ok = False
        
        while ok == False:
            try:
                position = input('Give the base point of the battleship: ')
                y = int(position[0]) -1
                x = ord(position[1].upper()) - ord('A') 
                direction = input('Give the direction of the battleship(h/v): ')
                if direction == 'h':
                    direction = 1
                if direction == 'v':
                    direction = -1    
                self._service.add_battleship(x, y, direction)
                ok = True
            except Exception as er:
                print("BAD INPUTS!\n", er)
            
    def place_cruiser(self):
        ok = False
        
        while ok == False:
            try:
                position = input('Give the base point of the cruiser: ')
                y = int(position[0]) -1
                x = ord(position[1].upper()) - ord('A') 
                direction = input('Give the direction of the cruiser(h/v): ')
                if direction == 'h':
                    direction = 1
                if direction == 'v':
                    direction = -1    
                self._service.add_cruiser(x, y, direction)
                ok = True
            except Exception as er:
                print("BAD INPUTS!\n", er)
                  
    def place_destroyer(self):
        ok = False
        
        while ok == False:
            try:
                position = input('Give the base point of the destroyer: ')
                y = int(position[0]) -1
                x = ord(position[1].upper()) - ord('A') 
                direction = input('Give the direction of the destroyer(h/v): ')
                if direction == 'h':
                    direction = 1
                if direction == 'v':
                    direction = -1    
                self._service.add_destroyer(x, y, direction)
                ok = True
            except Exception as er:
                print("BAD INPUTS!\n", er)
            
    def place_ships(self):
        self.place_battleship()
        self.show_my_board()
        self.place_cruiser()
        self.show_my_board()
        self.place_destroyer()
        self.show_my_board()
        
    def attack(self):
        ok = False
        
        while ok == False:
            try:
                position = input('Give the coordinate that you want to attack: ')
                y = int(position[0]) -1
                x = ord(position[1].upper()) - ord('A') 
                self._ai.miss_hit(x, y)
                ok = True
            except Exception as er:
                print("BAD INPUTS!\n", er)
                
    def warnings(self):
        print(self._ai.ship_distroyed())
        print(self._service.ship_distroyed())
        
        
                  
    def start(self):
        self.show_my_board()
        self._ai.ai_add_ships()
        self.place_ships()
        you_lose = self._service.game_over()
        ai_loses = self._service.game_over()
        
        while you_lose == False and ai_loses == False:
            self.show_my_board()
            self.show_ai_board()
            self.attack()
            self._ai.ai_attack(self._service)
            self.warnings()
            you_lose = self._service.game_over()
            ai_loses = self._ai.game_over()
            
        if you_lose == True:
            print("GAME OVER")
        else:
            print("YOU WON")


