from forex_python.converter import CurrencyRates
import random as rnd


def get_money_interval(difficulty_input):
    curr = CurrencyRates()
    rate = curr.get_rate('USD', 'ILS')
    return (rate-(5-difficulty_input), rate + (5-difficulty_input))



def get_guess_from_user(curr_interval):
    interval = curr_interval
    number = rnd.randint(1, 100)
    min_interval = number / interval[0]
    max_interval = number / interval[1]
    user_input = int(input("please tell us what is the amount in USD of "+str(number)+" ILS ?"))
    if max_interval <= user_input <= min_interval:
        results = True
        return results
    else:
        results = False
        return results


def play(difficulty_input):
    interval = get_money_interval(difficulty_input)
    guess = get_guess_from_user(interval)
    return guess
