# Currency Roulette Game - Lior A

def get_money_interval(difficulty,USD_amount):
    from currency_converter import CurrencyConverter
    t = round(CurrencyConverter().convert(USD_amount, 'USD', 'ILS'),2)
    #print(f't is: {t}')
    min = float(t-(5-difficulty))
    max = float(t+(5-difficulty))
    interval = (round(min,2),round(max,2))
    #print(f'Interval is: {interval}')
    return (interval)

def get_guess_from_user(USD_amount):
    guess = float(input(f'Please guess what is the value of {USD_amount}[USD] in ILS: '))
    if guess < 0:
        raise Exception("Your guess is negative! Try again")
    print(f'Guess is: {guess}')
    return (guess)

def play(difficulty):
    import random
    USD_amount = random.randint(1, 100)
    print(f'USD_amount: {USD_amount}')
    interval = get_money_interval(difficulty,USD_amount)
    if (interval[0]-0.01 < get_guess_from_user(USD_amount) < interval[1]+0.01):
        print ("*****  TRUE!!! You won! Play with us again  *****\n")
        return True
    else:
        print("**********    False. You lost! Try again.....    **********\n")
        return False