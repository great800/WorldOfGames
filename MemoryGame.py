# Memory Game - Lior A
import Utils

def generate_sequence(difficulty):
    # difficulty is the list length
    import random, time
    if difficulty < 1:
        raise Exception("List length is not valid!")
    list = [random.randint(1,101) for i in range(0, difficulty)]
    print("In 5 seconds number/s will appear for less than one second. Try to remember it/them. Ready? Steady? Go!")
    time.sleep(5)
    print(f'Remember these numbers: {list}')
    time.sleep(0.7)
    Utils.Screen_cleaner()
    return list

def get_list_from_user(difficulty):
    # difficulty is the size of the list length
    list = []
    print(f'Please try to repeat the {difficulty} numbers you have just seen:')
    for i in range (1,difficulty+1):
        a = int(input(f'{i}:'))
        if a < 1:
            raise Exception("Your number is out of range!")
        else:
            list.append(a)
    #print(f'Your list is: {list}')
    return list

def is_list_equal(list1, list2):
    if list1 == list2:
        return True
    else:
        return False

def play(difficulty):
    if (is_list_equal(generate_sequence(difficulty),get_list_from_user(difficulty))):
        print("*****  TRUE!!! You won! Play with us again  *****\n")
        return True
    else:
        print("**********    False. You lost! Try again.....    **********\n")
        return False





