from GuessGame import play as Guess_play
from MemoryGame import play as Memory_play
from CurrencyRouletteGame import play as Currency_play

# welcome message

def welcome():
    name = input("Take breath , get excited and say what your name  : \n ")
    print("Hello " + name + " and welcome to the World of Games (WoG)\n")

# game of choose and difficulty


def load_game():
    from pandas import DataFrame, options

    options.display.max_colwidth = 1

    g_dict = {
        1: " Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back  ",
        2: " Guess Game - guess a number and see if you chose like the computer                          ",
        3: " Currency Roulette - try and guess the value of a random amount of USD in ILS                "
    }

    d_dict = {
        1: "super easy",
        2: "easy",
        3: "normal",
        4: "difficult",
        5: "expert",


    }


    print("-----  ----- -----  ----- ")
    print(DataFrame.from_dict(g_dict, orient='index', columns=[""]))
    Game_Number = int(input("\nPlease choose a game to play: "))
    print("-----  ----- -----  ----- ")

    if 1 <= Game_Number <= 3:
        print("-----  ----- -----  ----- ")
        print("choose one of the following difficulties : \n ")
        print(DataFrame.from_dict(d_dict, orient='index', columns=["  Description"]))
        print("-----  ----- -----  ----- ")
        Difficult_Level = int(input("\nPlease make your selection now :  "))
        if 1 <= Difficult_Level <= 5:
            print("\nThe game will begin shortly")
            if Game_Number == 1:
                result = Memory_play(Difficult_Level)
                print(result)
            elif Game_Number == 2:
                result = Guess_play(Difficult_Level)
                print()
                print(result)

            elif Game_Number == 3:
                result = Currency_play(Difficult_Level)
                print(result)
        else:
            print("please chose a a valid difficultly")
    else:
        print("You did not choose a valid game please choose one")
