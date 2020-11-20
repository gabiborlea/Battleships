from Domain.board import Board
from Domain.ships import Battleship, Cruiser, Destoryer
from Infrastructure.repo import Repository
from Business.service import Service
from Business.ai import AI
from Presentation.ui import UI
from Presentation.gui import GUI

my_repo = Repository()
my_board = Board(my_repo)
service = Service(my_repo)
ai_repo = Repository()
empty_repo = Repository()
ai_board = Board(empty_repo)
hidden = Board(ai_repo)
ai = AI(ai_repo, empty_repo)

choice = input('UI/GUI: ')

if choice == 'UI':

    ui = UI(my_board, service, ai_board, ai, hidden)
    ui.start()

elif choice == 'GUI':
    g = GUI(service, ai, my_repo.get_data(), ai_repo.get_data())
    g.start()
    