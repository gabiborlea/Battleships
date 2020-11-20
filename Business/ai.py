import random
from Domain.ships import Battleship, Cruiser, Destoryer
from Infrastructure.repo import RepoError
class AI:
    def __init__(self, ships_repo, hidden_repo):
        self._ships_repo = ships_repo
        self._hidden_repo = hidden_repo
        self._destroyed_nr = 0
        self._pos_stack = []
        self._tries_for_1 = [[1,0], [0,1], [-1,0] , [0,-1]]
        self._nr_tries_1 = 0
        self._nr_tries_2 = 0
        self._nr_tries_3 = 0
        self._hit = 0
        
    def ai_add_ships(self):
        ok = False
        while ok == False:
            try:
                x = random.randrange(0,8)
                y = random.randrange(0,8)
                direction = random.choice([-1, 1])
                self._battleship = Battleship(x, y, direction)
                self._ships_repo.add_ship(self._battleship)
                ok = True
            except Exception:
                pass
            
        ok = False
        while ok == False:
            try:
                x = random.randrange(0,8)
                y = random.randrange(0,8)
                direction = random.choice([-1,1])
                self._cruiser = Cruiser(x, y, direction)
                self._ships_repo.add_ship(self._cruiser)
                ok = True
            except Exception:
                pass
            
        ok = False
        while ok == False:
            try:
                x = random.randrange(0,8)
                y = random.randrange(0,8)
                direction = random.choice([1,-1])
                self._destroyer = Destoryer(x, y, direction)
                self._ships_repo.add_ship(self._destroyer)
                ok = True
            except Exception:
                pass
            
            
    def ai_attack(self, service):
        '''
        ok = False
        while ok == False:
            try:
                x = random.randrange(0,8)
                y = random.randrange(0,8)
                service.miss_hit(y, x)
                ok = True
            except Exception:
                pass
        '''
        
        
        if service._cruiser.get_size() == -1:
            service._cruiser.set_size(-2) 
            self._hit = 0
            self._nr_tries_1 = 0
            self._nr_tries_2 = 0
            self._nr_tries_3 = 0
            self._pos_stack = []
            
        elif service._destroyer.get_size() == -1:
            service._destroyer.set_size(-2)
            self._hit = 0
            self._nr_tries_1 = 0
            self._nr_tries_2 = 0
            self._nr_tries_3 = 0
            self._pos_stack = []
            
        elif service._battleship.get_size() == -1:
            service._battleship.set_size(-2)
            self._hit = 0
            self._nr_tries_1 = 0
            self._nr_tries_2 = 0
            self._nr_tries_3 = 0
            self._pos_stack = []
        
        #####0
        elif self._hit == 0:
            
            ok = False
            while ok == False:
                try:
                    x = service._ships_repo.get_min_col()
                    y = random.randrange(8)
                    service.miss_hit(x, y)
                    if service._ships_repo.get_cood_info(x,y) == 'H':
                        self._hit = 1
                        self._pos_stack.append([x,y])
                    ok = True
                except Exception as er:
                    print(er)
                
            print(x,y)  
                
        #####1   
        elif self._hit == 1:
            pos = self._pos_stack[0]
            ok = False
            while ok == False:
                try:
                    x = pos[0] + self._tries_for_1[self._nr_tries_1][0]
                    y = pos[1] + self._tries_for_1[self._nr_tries_1][1]
                        
                        
                    service.miss_hit(x, y)
                    ok = True  
                        
                    if service._ships_repo.get_cood_info(x,y) == 'H':
                        self._hit = 2
                        self._pos_stack.append([x,y])
                        
                    self._nr_tries_1 += 1
                        
                except Exception:
                    self._nr_tries_1 += 1
                    
                    
                
        ####2              
        elif self._hit == 2:
            
            first = self._pos_stack[0]
            last = self._pos_stack[len(self._pos_stack)-1]
                
            if first[0] == last[0]:
                if first[1] > last[1]:
                    grater = first
                    lower = last
                        
                else:
                    grater = last
                    lower = first
                        
                if self._nr_tries_2 == 0:
                    try:
                        service.miss_hit(grater[0], grater[1]+1)
                        if service._ships_repo.get_cood_info(grater[0], grater[1]+1) == 'H':
                            self._hit = 3
                            self._pos_stack.append([grater[0], grater[1]+1])
                    except Exception:
                        self._nr_tries_2 += 1
                            
                if self._nr_tries_2 == 1:
                    service.miss_hit(lower[0], lower[1]-1)
                    if service._ships_repo.get_cood_info(lower[0], lower[1]-1) == 'H':
                        self._hit = 3
                        self._pos_stack.append([lower[0], lower[1]-1])
                
            elif first[1] == last[1]:
                if first[0] > last[0]:
                    grater = first
                    lower = last
                        
                else:
                    grater = last
                    lower = first
                        
                if self._nr_tries_2 == 0:
                    try:
                        service.miss_hit(grater[0]+1, grater[1])
                        if service._ships_repo.get_cood_info(grater[0]+1, grater[1]) == 'H':
                            self._hit = 3
                            self._pos_stack.append([grater[0]+1, grater[1]])
                    except Exception:
                        self._nr_tries_2 += 1
                            
                if self._nr_tries_2 == 1:
                    service.miss_hit(lower[0]-1, lower[1])
                    if service._ships_repo.get_cood_info(lower[0]-1, lower[1]) == 'H':
                        self._hit = 3
                        self._pos_stack.append([lower[0]-1, lower[1]])
          
        ####3
                    
        elif self._hit == 3:
            first = self._pos_stack[0]
            last = self._pos_stack[len(self._pos_stack)-1]
                
            if first[0] == last[0]:
                if first[1] > last[1]:
                    grater = first
                    lower = last
                        
                else:
                    grater = last
                    lower = first
                        
                if self._nr_tries_3 == 0:
                    try:
                        service.miss_hit(grater[0], grater[1]+1)
                        if service._ships_repo.get_cood_info(grater[0], grater[1]+1) == 'H':
                            self._hit = 4
                            self._pos_stack.append([grater[0], grater[1]+1])
                    except Exception:
                        self._nr_tries_3 += 1
                            
                if self._nr_tries_3 == 1:
                    service.miss_hit(lower[0], lower[1]-1)
                    if service._ships_repo.get_cood_info(lower[0], lower[1]-1) == 'H':
                        self._hit = 4
                        self._pos_stack.append([lower[0], lower[1]-1])
                
            elif first[1] == last[1]:
                if first[0] > last[0]:
                    grater = first
                    lower = last
                        
                else:
                    grater = last
                    lower = first
                        
                if self._nr_tries_3 == 0:
                    try:
                        service.miss_hit(grater[0]+1, grater[1])
                        if service._ships_repo.get_cood_info(grater[0]+1, grater[1]) == 'H':
                            self._hit = 4
                            self._pos_stack.append([grater[0]+1, grater[1]])
                    except Exception:
                        self._nr_tries_3 += 1
                            
                if self._nr_tries_3 == 1:
                    service.miss_hit(lower[0]-1, lower[1])
                    if service._ships_repo.get_cood_info(lower[0]-1, lower[1]) == 'H':
                        self._hit = 4
                        self._pos_stack.append([lower[0]-1, lower[1]])
                    
            
 
            
    def miss_hit(self, x, y):
        cood = self._ships_repo.get_cood_info(x,y)
        if cood == 'B':
            self._battleship.destroy() 
            self._ships_repo.add_miss_hit(x,y, 'H')
            self._hidden_repo.add_miss_hit(x,y, 'H')
        elif cood == 'C':
            self._cruiser.destroy()
            self._ships_repo.add_miss_hit(x,y, 'H')
            self._hidden_repo.add_miss_hit(x,y, 'H')
            
        elif cood == 'D':
            self._destroyer.destroy()
            self._ships_repo.add_miss_hit(x,y, 'H')
            self._hidden_repo.add_miss_hit(x,y, 'H')
        else:
            self._ships_repo.add_miss_hit(x,y, 'M')
            self._hidden_repo.add_miss_hit(x,y, 'M')
            
    def ship_distroyed(self):
        warning = ""
        if self._battleship.get_size() == 0:
            self._battleship.destroy()
            warning += "Battleship is destroyed"
            self._destroyed_nr += 1
            
        if self._cruiser.get_size() == 0:
            self._cruiser.destroy()
            warning += "Cruiser is destroyed"
            self._destroyed_nr += 1
        
        if self._destroyer.get_size() == 0:
            self._destroyer.destroy()
            warning += "Destroyer is destroyed"
            self._destroyed_nr += 1
            
        return warning
            
    def game_over(self):
        if self._destroyed_nr == 3:
            return True
        else:
            return False
