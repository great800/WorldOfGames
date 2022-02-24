import GuessGame
import MemoryGame
import CurrencyRouletteGame
import Score

def welcome(name):
    print (f'Hello {name} and welcome to the World of Games (WoG). \nHere you can find many cool games to play.\n')

def load_game():
     from GuessGame import play
     from MemoryGame import play
     from CurrencyRouletteGame import play

     try:
         user = str(input(f'Hi!\nWhat is your name please?\n'))
         welcome(user)
         game_number = int(input("Please choose a game to play (if you don't want to play - choose 4):\n"
         "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
         "2. Guess Game - guess a number and see if you chose like the computer\n"
         "3. Currency Roulette - try and guess the value of a random amount of USD in ILS\n"
         "4. Exit game\n"))
         while game_number < 1 or game_number > 4:
             raise Exception ('WRONG!!! Game Number has to be between 1 to 4. Try again')
         if game_number == 4:
             print ("Thank you and come to visit us again whenever you want :-)\n")
             return False, user

         level_of_difficulty = int(input("Please choose game difficulty from 1 to 5:\n"))
         while level_of_difficulty < 1 or level_of_difficulty > 5:
             raise Exception('WRONG!!! Level of Difficulty has to be between 1 to 5. Try again')
         if game_number == 1:
             if(MemoryGame.play(level_of_difficulty)):
                 Score.add_score(level_of_difficulty,user)
                 return True, user

         elif game_number == 2:
             if(GuessGame.play(level_of_difficulty)):
                 Score.add_score(level_of_difficulty,user)
                 return True, user
         elif game_number == 3:
             if(CurrencyRouletteGame.play(level_of_difficulty)):
                 Score.add_score(level_of_difficulty,user)
                 return True, user

     except Exception as e:
         print(e)

