from texttable import Texttable
class Board:
    def __init__(self, board_repo ):
        self._data = board_repo

        
        
    def __str__(self):
        table = Texttable()
        for idx in range(8):
            table.add_row(self._data.get_data()[idx][:])
            
        return table.draw()
