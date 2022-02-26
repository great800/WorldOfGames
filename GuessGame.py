# Guess Game - Lior A

def generate_number(difficulty):
    import random
    secret_number = random.randint(1,difficulty)
    return secret_number

def get_guess_from_user(difficulty):
    num = int(input(f'Please guess the number between 1 to {difficulty} the computer generated: '))
    if num < 1 or num > difficulty:
        raise Exception("Your number is out of range")
    return num

def compare_results(difficulty):
    user = get_guess_from_user(difficulty)
    comp = generate_number(difficulty)
    print(f'You chose: {user}')
    print(f'Computer chose: {comp}')
    if user == comp:
        return True
    else:
        return False

def play(difficulty):
    if(compare_results(difficulty)):
        print("*****  TRUE!!! You won! Play with us again  *****\n")
        return True
    else:
        print("**********    False. You lost! Try again.....    **********\n")
        return False

