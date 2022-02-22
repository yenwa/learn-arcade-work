import random





def main():
    print('Welcome to Camel!')
    print('You have stolen a camel to make your way across the great Mobi desert.')
    print('The natives want their camel back and are chasing you down! Survive your')
    print('desert trek and out run the natives.')

    done = False

    miles_traveled = 30
    thirst = 0
    camel_tiredness = 0
    natives_distance_traveled = 15
    drinks_in_the_canteen = 4
    miles_between = 0


    while not done:
        user_input = input('A. Drink from your canteen. \nB. Ahead moderate speed. \nC. Ahead full speed. \nD. '
                           'Stop for the night. \nE. Status check. \nQ. Quit. \nWhat is your choice? ')
        if user_input.upper() == 'Q':
            done = True
            print("Game over hope you had fun!")
        elif user_input.upper() == 'E':

            miles_between = miles_traveled - natives_distance_traveled

            print('Miles traveled: ', miles_traveled, '\ndrinks in the canteen: ', drinks_in_the_canteen, '\nThe natives are ', miles_between, 'miles behind you.')
        elif user_input.upper() == 'D':
            print('the camel is happy')
            camel_tiredness = 0

            for natives_distance_traveled_1 in random.choices(range(7, 16)):
                natives_distance_traveled = natives_distance_traveled + natives_distance_traveled_1


                print()

        elif user_input.upper() == 'C':
            for miles_traveled_1 in random.choices(range(10, 21)):
                miles_traveled = miles_traveled + miles_traveled_1

                print('You have traveled ', miles_traveled, 'miles.')
                thirst = thirst + 1
            for camel_tiredness_1 in random.choices(range(1, 4)):
                camel_tiredness = camel_tiredness_1 + camel_tiredness
                print()

            for natives_distance_traveled in random.choices(range(7, 16)):
                print()
        elif user_input.upper() == 'B':
            for miles_traveled_2 in random.choices(range(5, 13)):

                miles_traveled = miles_traveled + miles_traveled_2
                print('You have traveled ', miles_traveled, 'miles.')
                thirst = thirst + 1
                camel_tiredness = camel_tiredness + 1
        elif user_input.upper() == 'A':

                drinks_in_the_canteen = drinks_in_the_canteen - 1
                thirst = 0
        if drinks_in_the_canteen <= 1:
                print("Error you don't have enough drinks in the canteen in the canteen game over")
                done = True

        if thirst >= 4:
            print('you are thirsty')
            if thirst > 6:
                done = True
                print('You died of thirst')


        elif camel_tiredness >= 5:

            print('camel is tired')
        if camel_tiredness >= 8:
                done = True
                print('the camel is dead')
        if miles_traveled >= 200:
            done = True
            print('You won')
        if miles_traveled - natives_distance_traveled <= 0:
            done = True
            print('Game over the native caught up !')

# I'm kind of confused here I need to find out why

        if miles_traveled - natives_distance_traveled < 15:
                print('The natives are getting close ')











        #print()

main()


