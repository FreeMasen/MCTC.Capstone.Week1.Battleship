from src.player import Player
from src.ship import Ship
from src.direction import Direction
from src.cell_state import CellState
from src.intro import Intro
from random import randint

from src.consts import *

class Game():
    def __init__(self, two_payer = False):
        self.player_one = Player()
        self.player_two = Player()
        self.first_players_turn = True
        self.two_player = two_payer

    def welcom_user(self):
        clear()
        intro = Intro()
        print(intro.banner() + '\n')
        if self.__ask_bool__('Would you like to start with a tutorial?'):
            print(intro.rules())

    def setup(self):
        print('Let place Player 1\'s ships!')
        if (not self.__ask_bool__('Would you like me to place your ships for you?')):
            self.__setup_player__(self.player_one)
        else:
            self.__auto_setup__(self.player_one)
        if (self.two_player):
            self.__setup_player__(self.player_two)
        else:
            self.__auto_setup__(self.player_two)
        clear()
        print(figlet.renderText('Let\'s go!'))

    def take_turn(self):
        offender = self.player_two
        defender = self.player_one
        if self.first_players_turn:
            offender = self.player_one
            defender = self.player_two
        if not self.two_player and not self.first_players_turn:
            self.__auto_turn__(offender, defender)
        else:
            while (True):
                print(offender.display_board() + '\n')
                try:
                    x, y = self.__ask_for_target__()
                    if (y < 0 or y > 9): raise ValueError()
                except Exception as e:
                    print(figlet.renderText('Invalid target'))
                    print('The your target must be one letter and one number i.e. A1\n')
                    continue
                bomb_result = defender.board.bomb_square(x, y)
                if bomb_result == CellState.Invalid:
                    print(figlet.renderText('Invalid target'))
                    print('have you already played there?')
                    continue
                if bomb_result == CellState.Hit:
                    print(figlet.renderText(defender.mark_hit(x, y)))
                elif bomb_result == CellState.Missed:
                    print(figlet.renderText(('Miss!')))
                offender.board.offense.mark(x, y, bomb_result)
                break
        self.first_players_turn = not self.first_players_turn
        return self.__check_for_continue__()
        
    def __display_status__(self, last_result):
        return wrap_in_box(side_by_side(figlet.renderText('Last shot'), figlet.renderText(last_result), 'Ships', self.__ship_table__()))

    def __ship_table__(self):
        p1_ships = 'Your ships\n'
        p2_ships = 'Their ships'
        for name, ship in self.player_one.ships.items():
            p1_ships += '%s: %s/%s\n'% (name, ship.hits, ship.size)
        for name, ship in self.player_two.ships.items():
            p2_ships += '%s: %s/%s\n'% (name, ship.hits, ship.size)
        p1_lines = p1_ships.split('\n')
        p2_lines = p2_ships.split('\n')
        p1_width = max(map(lambda line: len(line), p1_lines))
        p2_width = max(map(lambda line: len(line), p2_lines))
        p1_lines[0] = p1_lines[0].center(p1_width)
        p2_lines[0] = p1_lines[0].center(p2_width)
        ret = ''
        p1_height = len(p1_lines)
        p2_height = len(p2_lines)
        target_height = max([p1_height, p2_height])
        for i in range(target_height):
            left = p1_lines[i] if i < p1_height else ' ' * p1_width
            right = p2_lines[i] if i < p2_height else ' ' * p2_width
            ret += left + '  ' + right
        return wrap_in_box(ret)
        

    def play_again(self):
        return self.__ask_bool__('Would you like to play again?')
    #setup
    def __setup_player__(self, player):
        #loop over the player's ship dictionary
        for name, ship in player.ships.items():
            #while the ship has not yet been placed
            while (not ship.placed):
                #Ask the user for the ships orientaton
                direction = self.__get_direction__('Would you like %s (%s) to be placed vertically? [y/n]' % (name, ship.size))
                #Calculate the x limit, this is needed incase the user wants to place part of the ship off the board
                x_limit = 10 - ship.size if direction == Direction.Horizontal else 10
                #Ask for the X axis position
                start_x = self.__get_coordinate__('Where would you like to start %s (%s) on the x axis? [A-%s]' % (name, ship.size, letters[x_limit - 1]), x_limit, True)
                #Calculate the y limit (see x_limit)
                y_limit = 10 - ship.size if direction == Direction.Vertical else 10
                #then ask for the Y axis position
                start_y = self.__get_coordinate__('Where would you like to start %s on the y axis? [1-%s]' % (name, y_limit), y_limit)
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

    def __auto_setup__(self, player, is_computer = True):
        player_name = 'the computer' if is_computer else 'player_one'
        print('Setting up %s\'s board' % player_name)
        for name, ship in player.ships.items():
            while (not ship.placed):
                direction_int = randint(0,1)
                direction = Direction.Vertical if (direction_int > 0) else Direction.Horizontal
                x_limit = 10 - ship.size if ship.direction == Direction.Horizontal else 10
                start_x = randint(0, x_limit)
                y_limit = 10 - ship.size if ship.direction == Direction.Vertical else 10
                start_y = randint(0, y_limit)
                ship.place(start_x, start_y, direction)
                if not player.board.place_ship(ship):
                    ship.clear_placement()



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
    #play
    def __auto_turn__(self, offender, defender):
        while (True):
            move_x = randint(0,9)
            move_y = randint(0,9)
            bomb_result = defender.board.bomb_square(move_x, move_y)
            if (bomb_result == CellState.Invalid):
                continue
            result = 'hit' if bomb_result == CellState.Hit else 'miss'
            print('Computer plays %s%s scores a %s.' % (letters[move_x], move_y, result))
            break
    
    def __ask_for_target__(self):
        target = self.__ask_chars__('What is your next target?', 2, 3)
        x_char = target[0]
        x = numbers[x_char]
        y_chars = ''.join(target[1:])
        y = int(y_chars)
        clear()
        return (x, y - 1)

    def __check_for_continue__(self):
        if self.player_one.has_lost():
            print('Player two wins!')
            return False
        if self.player_two.has_lost():
            print('Player one wins!')
            return False
        return True
    
    #interaction
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
    
    def __ask_chars__(self, message, min_length, max_length = None):
        if (max_length is None): max_length = min_length
        while (True):
            response = self.__ask__(message)
            res_len = len(response)
            if res_len < min_length:
                print('Sorry the input must be at least %s letter(s).' % length)
                continue
            if res_len > max_length:
                print('Sorry, the input must be less than %s', max_length + 1)
                continue
            chars = response[0:max_length]
            return tuple(chars)

    def __ask__(self, question):
        try:
            return input(question + '\n')
        except Exception as e:
            self.exit()
    
    def exit(self):
        print('Thanks for playing!')
        sys.exit()

