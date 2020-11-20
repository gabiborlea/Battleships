import pygame
pygame.font.init()
class GUI(object):
    def __init__(self, service, ai, my_data, ai_data):
        self._width = 800
        self._grid_width = self._width- (self._width)//4
        self._block_size = self._grid_width//8
        self._window = pygame.display.set_mode((self._width * 2, self._width))
        self._my_data = my_data
        self._ai_data = ai_data
        self._top_x_1 = (self._width - self._grid_width)/2
        self._top_y_1 = (self._width - self._grid_width)/2
        
        self._top_x_2 = self._width + (self._width - self._grid_width)/2
        self._top_y_2 = (self._width - self._grid_width)/2
        
        self._mouse = pygame.mouse.get_pos()
        
        self._service = service
        self._ai = ai
        self._direction = 1
        self._ai_warning = ""
        self._my_warning = ""
        
    def draw_rect(self, color, i, j, x, y):
        pygame.draw.rect(self._window, color, (x + j*self._block_size, y + i*self._block_size, self._block_size, self._block_size), 0)
    
        
    def draw_my_grid(self):
        for i in range(len(self._my_data)):
            for j in range(len(self._my_data[i])):
                if self._my_data[i][j] == ' ':
                    self.draw_rect((225,225,225), i, j, self._top_x_1, self._top_y_1)
                elif self._my_data[i][j] == 'M':
                    self.draw_rect((0,0,255), i, j, self._top_x_1, self._top_y_1)
                    
                elif self._my_data[i][j] == 'H':
                    self.draw_rect((255,0,0), i, j, self._top_x_1, self._top_y_1)    
                
                else:
                    self.draw_rect((180,255,100), i, j, self._top_x_1, self._top_y_1)
                    
        if self._placed == 0:         
            self.hover_ship(self._direction, self._top_x_1, self._top_y_1, 4)
            
        elif self._placed == 1:         
            self.hover_ship(self._direction, self._top_x_1, self._top_y_1, 3)
            
        elif self._placed == 2:
            self.hover_ship(self._direction, self._top_x_1, self._top_y_1, 2)          
                    
        
                    
                    
        for i in range(len(self._my_data) + 1): 
            x = self._top_x_1
            y = self._top_y_1 
            pygame.draw.line(self._window, (0,0,0), (x, y + i*self._block_size), (x+ self._grid_width, y + i*self._block_size), 2)
            pygame.draw.line(self._window, (0,0,0), (x + i*self._block_size, y), (x + i*self._block_size, y + self._grid_width), 2)
            
        
        letter = 'A'
        number = '1'
        for i in range(len(self._my_data)):  
            font = pygame.font.SysFont('comicsans', 60)
            label = font.render(letter, True, (0,0,0))
            self._window.blit(label, (self._top_x_1 + i*self._block_size + 25, self._top_y_1 - 40))
            letter = chr(ord(letter) + 1) 
            
            label_1 = font.render(number, True, (0,0,0))
            self._window.blit(label_1, (self._top_x_1 - 40, self._top_y_1 + self._block_size * i + 20 ))
            number = chr(ord(number) + 1)
            
    def draw_ai_grid(self):
        for i in range(len(self._ai_data)):
            for j in range(len(self._ai_data[i])):
                    
                if self._ai_data[i][j] == 'M':
                    self.draw_rect((0,0,255), i, j, self._top_x_2, self._top_y_2)
                    
                elif self._ai_data[i][j] == 'H':
                    self.draw_rect((255,0,0), i, j, self._top_x_2, self._top_y_2)
                    
                else:
                    self.draw_rect((225,225,225), i, j, self._top_x_2, self._top_y_2)

                    
        self.hover_box(self._top_x_2, self._top_y_2)
                    
        for i in range(len(self._ai_data) + 1): 
            x = self._top_x_2
            y = self._top_y_2 
            pygame.draw.line(self._window, (0,0,0), (x, y + i*self._block_size), (x + self._grid_width, y + i*self._block_size), 2)
            pygame.draw.line(self._window, (0,0,0), (x + i*self._block_size, y), (x + i*self._block_size, y + self._grid_width), 2)
            
        letter = 'A'
        number = '1'
        for i in range(len(self._my_data)):  
            font = pygame.font.SysFont('comicsans', 60)
            label = font.render(letter, True, (0,0,0))
            self._window.blit(label, (self._top_x_2 + i*self._block_size + 25, self._top_y_2 - 40))
            letter = chr(ord(letter) + 1) 
            
            label_1 = font.render(number, True, (0,0,0))
            self._window.blit(label_1, (self._top_x_2 - 40, self._top_y_2 + self._block_size * i + 20 ))
            number = chr(ord(number) + 1)
            
    def hover_box(self, x, y):
        for i in range(len(self._ai_data)):
            for j in range(len(self._ai_data)):
                if (x + j*self._block_size + self._block_size) > self._mouse[0] > x + j*self._block_size and y + i*self._block_size + self._block_size > self._mouse[1] > y + i*self._block_size:
                    if self._ai_data[i][j] == ' ':
                        self.draw_rect((200,200,200), i, j, x, y)
                    elif self._ai_data[i][j] == 'M':
                        self.draw_rect((0,0,255), i, j, self._top_x_2, self._top_y_2)
                    
                    elif self._ai_data[i][j] == 'H':
                        self.draw_rect((255,0,0), i, j, self._top_x_2, self._top_y_2)
                    else:
                        self.draw_rect((200,200,200), i, j, x, y)
        
        
    def hover_ship(self, direction, x, y, size):
        if direction == 1:
            for i in range(size-1, 8):
                for j in range(8):
                    if (x + j*self._block_size + self._block_size) > self._mouse[0] > x + j*self._block_size  and y + i*self._block_size + self._block_size > self._mouse[1] > y + i*self._block_size:
                        for idx in range(size):
                            self.draw_rect((180,255,100), i-idx, j, x, y)
                        
        elif direction == -1:
            for i in range(8):
                for j in range(size-1, 8):
                    if (x + j*self._block_size + self._block_size) > self._mouse[0] > x + j*self._block_size and y + i*self._block_size + self._block_size > self._mouse[1] > y + i*self._block_size:
                        for idx in range(size):
                            self.draw_rect((180,255,100), i, j-idx, x, y)
    

                        
    def place_ship(self, size):
        x = self._top_x_1
        y = self._top_y_1
        placed = False
        if self._direction == 1:
            for i in range(size -1, 8):
                for j in range(8):
                    if (x + j*self._block_size + self._block_size) > self._mouse[0] > x + j*self._block_size  and y + i*self._block_size + self._block_size > self._mouse[1] > y + i*self._block_size:
                        if size == 4:
                            self._service.add_battleship(j,i,1)
                            
                        elif size == 3:
                            self._service.add_cruiser(j,i,1)
                        
                        elif size == 2:
                            self._service.add_destroyer(j,i,1)
                        placed = True
                            
                        
        elif self._direction == -1:
            for i in range(8):
                for j in range(size-1, 8):
                    if (x + j*self._block_size + self._block_size) > self._mouse[0] > x + j*self._block_size and y + i*self._block_size + self._block_size > self._mouse[1] > y + i*self._block_size:
                        if size == 4:
                            self._service.add_battleship(j,i,-1)
                            
                        elif size == 3:
                            self._service.add_cruiser(j,i,-1)
                        
                        elif size == 2:
                            self._service.add_destroyer(j,i,-1)
                            
                        placed = True
                        
        if placed == False:
            raise ValueError("incorect position")
                            
                            
    def my_attack(self):
        x = self._top_x_2
        y = self._top_y_2
        self._attacked = False
        for i in range(8):
            for j in range(8):
                if (x + j*self._block_size + self._block_size) > self._mouse[0] > x + j*self._block_size and y + i*self._block_size + self._block_size > self._mouse[1] > y + i*self._block_size:
                    try:
                        self._ai.miss_hit(j,i)
                        self._attacked = True
                    except Exception:
                        pass
                    
    def ai_attack(self):
        self._ai.ai_attack(self._service)
        
    def warnings(self):
        ai_text = self._ai.ship_distroyed()
        if ai_text !=  "":
            self._ai_warning = ai_text
            
        font = pygame.font.SysFont('comicsans', 30)
        ai_warning = font.render(self._ai_warning, True, (0,0,0))
        text_poz = ai_warning.get_rect()
        text_poz.center = (self._width + self._width//2, 750)
        self._window.blit(ai_warning, text_poz )
        
        
        my_text = self._service.ship_distroyed()
        if my_text !=  "":
            self._my_warning = my_text
            
        my_warning = font.render(self._my_warning, True, (0,0,0))
        text_poz = my_warning.get_rect()
        text_poz.center = (self._width//2, 750)
        self._window.blit(my_warning, text_poz )
        
        if self._ai.game_over() == True:
            font = pygame.font.SysFont('comicsans', 50)
            won = font.render('YOU WON', True, (0,0,0))
            text_poz = won.get_rect()
            text_poz.center = ((self._width + self._width)//2, 50)
            self._window.blit(won, text_poz )
            
        elif self._service.game_over() == True:
            font = pygame.font.SysFont('comicsans', 50)
            won = font.render('YOU LOSE', True, (0,0,0))
            text_poz = won.get_rect()
            text_poz.center = ((self._width + self._width)//2, 50)
            self._window.blit(won, text_poz )
    
        
    def redraw_window(self):
        self._window.fill((240,0,255))
        if self._placed == 4:
            self.warnings()
        self.draw_my_grid()
        self.draw_ai_grid()
        pygame.display.update()
        
        
        
        
    def start(self):
        run = True
        self._placed = 0
        while run:
            
            self._mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                
                if event.type == pygame.KEYDOWN:  
                    if event.key == pygame.K_UP:
                        self._direction = 1
                    
                    if event.key == pygame.K_LEFT:
                        self._direction = -1 
                        
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self._placed == 0:
                        try:
                            self.place_ship(4)
                            self._placed += 1
                        except ValueError:
                            pass    
                        
                        
                    elif self._placed == 1:
                        try:
                            self.place_ship(3)    
                            self._placed += 1 
                        except ValueError:
                            pass 
                        
                    elif self._placed == 2:
                        try:
                            self.place_ship(2)
                            self._placed += 1  
                        except ValueError:
                            pass  
                        
                if self._placed == 3:
                    self._ai.ai_add_ships()
                    self._placed += 1
                    
                if self._placed == 4:
                        
                    if event.type == pygame.MOUSEBUTTONDOWN and self._top_x_2 + self._grid_width> self._mouse[0] > self._top_x_2 and self._top_y_2 + self._grid_width> self._mouse[1] > self._top_y_2:
                        if self._service.game_over() == False and self._ai.game_over() == False:
                            self.my_attack()
                            if self._attacked == True:
                                self.ai_attack()
                            
                    
                        
                                      
                    
                
            self.redraw_window()
        
