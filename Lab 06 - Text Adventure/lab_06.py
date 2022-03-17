class Room():

    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    room_list = []


    # room define
    room = Room('You are in a building and standing in the Main hall.\nThere is passage to the bedroom to the East'
                '\nThere is a door at the South to the Kitchen\nThere is another door to the balcony to the West', None, 1, 2, 3)
    room_list.append(room)




# current room
    current_room = 0


    # setting done to false
    done = False


    while done == False:
        current_room = 0

        print('\n')

        print(room_list[0].description)

        input_1 = input('\nWhat direction will you like to go ?\nPress Q to quit ')



        if input_1.upper() == 'N':

            next_room = room_list[current_room].north

            if next_room == None:
                print('\nNO not that way you are already at the main hall :(')

            else:
                current_room = next_room

        elif input_1.upper() == 'S':
            next_room = room_list[current_room].south

            print('\nNow here you are, at the Kitchen !')

            if next_room == None:
                print('\nNO not that way :(')

            else:
                current_room = next_room

        elif input_1.upper() == 'E':
            next_room = room_list[current_room].east

            print('\nOh you made it to the Bedroom nice job !')

            if next_room == None:
                print('\nNO not that way :(')

            else:
                current_room = next_room

        elif input_1.upper() == 'W':
            next_room = room_list[current_room].west

            print('\nGreat ! You are now at the balcony. ')

            if next_room == None:
                print('\nNO not that way :(')

            else:
                current_room = next_room

        elif input_1.upper() == 'Q':
            print('\nYou have end the game hope you had fun :)')
            done = True

        else:
            print("\nEnter a valid input \nPress E to go to the Bedroom"
                  "\nPress S to go to the Kitchen\nPress W to go to the Balcony")







main()











