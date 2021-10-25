import random as rnd

# Secret number

# generate a random number


def generate_number(difficulty_input):
    number = rnd.randint(1, difficulty_input)
    return number


# getting a guessed number from player


def get_guess_from_user(difficulty_input):
    guess = int(input("\nPlease choose a number between 1 and " + str(difficulty_input)))
    return guess


# comparing results


def compare_results(guess_number,sect_number):

    if sect_number == guess_number:
        result = True
        return result
    else:
        result = False
        return result





def play(difficulty_input):
    secret_number = generate_number(difficulty_input)
    guessed_number = get_guess_from_user(difficulty_input)
    result = compare_results(guessed_number, secret_number)
    return result


