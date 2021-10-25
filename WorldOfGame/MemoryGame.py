import random as rnd
from time import sleep
import os

def clear():

    print ("\n" * 100)


def generate_sequence(diffculty):
    # random.sample(sequence(range or list ,tuple .....), length)
    g_list = rnd.sample(range(1,101),diffculty)
    return g_list

def get_list_from_user(difficulty_input):
    user_list_input = input(f"PLEASE ENTER THE {difficulty_input} DISAPPEAR NUMBERS FROM THE SCREEN : ")
    # Using split() method :
    # This function helps in getting multiple inputs from users
    user_list = user_list_input.split()

    while len(user_list) != difficulty_input:
        if len(user_list) != difficulty_input:
            print(
                "You have entered " + str(len(user_list)) + " values please enter " + str(difficulty_input) + " values")
            user_list_input = input("Please enter " + str(difficulty_input) + " numbers")
            user_list = user_list_input.split()
    else:
        return user_list

def is_list_equal(random_seq, user_input):
    rnd_list = random_seq
    user_seq = user_input
    user_seq = list(map(int, user_seq))
    if rnd_list == user_seq:
        result = True
        return result
    else:
        result = False
        return result


def play(difficulty_input):
    rnd_list = generate_sequence(difficulty_input)
    print("\nthe numbers are : "+str(rnd_list))
    sleep(1)
    # system('cls')
    clear()
    user_list = get_list_from_user(difficulty_input)
    result = is_list_equal(rnd_list, user_list)
    return result
