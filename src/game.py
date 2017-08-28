from src.player import Player
from src.ship import Ship
from src.direction import Direction
from src.grid import letters
from src.cell_state import CellState
from random import randint
import sys

#map of letters to indicies
numbers = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

class Game():
    def __init__(self, two_payer = False):
        self.player_one = Player()
        self.player_two = Player()
        self.first_players_turn = True
        self.game_over = False
        self.two_player = two_payer

    def setup(self):
        print('Let place Player 1\'s ships!')
        if (not self.__ask_bool__('Auto-place?')):
            self.__setup_player__(self.player_one)
        else:
            self.__auto_setup__(self.player_one)
        if (self.two_player):
            self.__setup_player__(self.player_two)
        else:
            self.__auto_setup__(self.player_two)

    def take_turn(self):
        offender = self.player_two
        defender = self.player_one
        if self.first_players_turn:
            offender = self.player_one
            defender = self.player_two
        if self.two_player and not self.first_players_turn:
            self.__auto_turn__(offender, defender)
        else:
            valid_input = False
            while (True):
                print(offender.board.offense.display() + '\n')
                target = self.__ask_chars__('What is your next target?\n', 2)
                try:
                    x = numbers[target[0].lower()]
                    y = int(target[1])
                except Exception as e:
                    print('The your target must be one letter and one number i.e. A1\n')
                    continue
                bomb_result = defender.board.bomb_square(x, y)
                if (CellState.Invalid):
                    print('Invalid position, try again')
                    continue
                offender.board.offense.mark(x, y, bomb_result)
        self.first_players_turn = not self.first_players_turn

    #setup
    def __setup_player__(self, player):
        #loop over the player's ship dictionary
        for name, ship in player.ships.items():
            #while the ship has not yet been placed
            while (not ship.placed):
                #Ask the user for the ships orientaton
                direction = self.__get_direction__('Would you like %s (%s) to be placed vertically? [y/n]\n' % (name, ship.size))
                #Calculate the x limit, this is needed incase the user wants to place part of the ship off the board
                x_limit = 10 - ship.size if direction == Direction.Horizontal else 10
                #Ask for the X axis position
                start_x = self.__get_coordinate__('Where would you like to start %s (%s) on the x axis? [A-%s]\n' % (name, ship.size, letters[x_limit - 1]), x_limit, True)
                #Calculate the y limit (see x_limit)
                y_limit = 10 - ship.size if direction == Direction.Vertical else 10
                #then ask for the Y axis position
                start_y = self.__get_coordinate__('Where would you like to start %s on the y axis? [1-%s]\n' % (name, y_limit), y_limit)
                ship.place(start_x, start_y, direction)
                # try and place the ship
                if (player.board.place_ship(ship)):
                    #if successful, ask the user to confirm
                    ship.placed = self.__validate_placement__(player, name, ship)
                    #if the user said no
                    if (not ship.placed):
                        #restat the placement
                        player.board.remove_ship(ship)
                        ship.clear_placement()
                else:
                    #if not successful, start from the top with this ship
                    print('Sorry, stacking your ships would be cheating\n')

    def __auto_setup__(self, player):
        print('Setting up the computer\'s board')
        for name, ship in player.ships.items():
            print('placing %s' % name)
            while (not ship.placed):
                direction = randint(0,1)
                ship.direction = Direction.Vertical if (direction > 0) else Direction.Horizontal
                x_limit = 10 - ship.size if ship.direction == Direction.Horizontal else 10
                ship.start_x = randint(0, x_limit)
                y_limit = 10 - ship.size if ship.direction == Direction.Vertical else 10
                ship.start_y = randint(0, y_limit)
                ship.placed = player.board.place_ship(ship)
        print('computer board set')



    def __validate_placement__(self, player, name, ship):
        print(player.board.defense.display())
        x = letters[ship.coordinates[0][0]]
        y = ship.coordinates[0][1] + 1
        return self.__ask_bool__('You want to place your %s at [%s, %s] going %sly? [y/n]' % (name, x, y, ship.direction.value))
    
    def __get_direction__(self, message):
        #ask if the placement should be vertical
        is_vertical = self.__ask_bool__(message)
        #return the result
        if (is_vertical):
            return Direction.Vertical
        else:
            return Direction.Horizontal

    def __get_coordinate__(self, message, upper, x = False):
        #loop until return
        while (True):
            if (x):
                chars = self.__ask_chars__(message, 1)[0]
                print(chars)
                char = chars[0]
                try:
                    return numbers[char.lower()]
                except Exception as e:
                    pass
            else:
                #ask for the value from the user
                coordinate = self.__ask_int__(message)
                #if the value is in the right range
                if (coordinate <= upper and coordinate > 0):
                    #return the coordinate as an index value (minus 1), ending the loop
                    return coordinate - 1
            #if we made it here, display the error message and the loop will start again
            print('Sorry, it would be unfair to place this ship off the grid\n')

    def __ask_bool__(self, message):
        #loop until return
        while (True):
            #ask the question
            res = self.__ask__(message)
            #if the length of the response is less than 1
            if len(res) < 1:
                #display the error message and start the loop again
                print('Sorry, I need a y or an n')
                continue
            #if the response starts with a y
            if res[0].lower() == 'y':
                return True
            #if the response starts with an n
            elif res[0].lower() == 'n':
                return False
            #if we haven't retuned, display the error message and
            #the loop will restart
            print('Sorry, I need a y or an n')

    def __ask_int__(self, message):
        #loop until return
        while (True):
            try:
                #try and get the input as an int, 
                #if no error is raised, return the value
                return int(self.__ask__(message))
            except Exception as e:
                #if an erro is raised, display the error message 
                #and the loop will start again
                print('Sorry I need a number')
    
    def __ask_chars__(self, message, length):
        while (True):
            response = self.__ask__(message)
            if (len(response) == length):
                print('returning %s positions 0 through %s' % (response, length - 1))
                chars = response[0:length]
                return tuple(chars)
            print('Sorry the input must be a %s letter(s).' % length)
    
    #play
    def __auto_turn__(self, offender, defender):
        print('Calculating computer\'s move.')
        while (True):
            move_x = randint(0,9)
            move_y = randint(0,9)
            bomb_result = defender.board.bomb_square(move_x, move_y)
            if (bomb_result == CellState.Invalid):
                continue
            result = 'hit' if bomb_result == CellState.Hit else 'miss'
            print('Computer plays %s%s scores a %s.' (letters[move_x], move_y, result))
    
    def __ask__(self, question):
        try:
            return input(question + '\n')
        except Exception as e:
            self.__exit__()
    
    def __exit__(self):
        print('Thanks for playing!')
        sys.exit()