# import random

# Define your GuessingGame class here...
# class GuessingGame():
#     def __init__(self, answer):
#         self.answer = answer
#     @property
#     def answer_lock(self):
#        return self.answer

#Write a function to take user input "guess" and 
#compare it to the value of our GuessingGame class "answer".
    
# ----- main.py -----
# def gameTime():
#     game = GuessingGame(random.randint(1,100))
#     last_guess  = None
#     last_result = None

#     while game.solved() == False:
#         if last_guess != None: 
#             print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
#             print("")

#     last_guess  = input("Enter your guess: ")
#     last_result = game.guess(last_guess)


#     print(f"{last_guess} was correct!")

import random
class GuessingGame():

    def __init__(self, answer):
        self.answer = answer
        print("Guess the number I am thinking of, or else: ")

    def guess(self):
        user_guess = int(input("Enter your guess: "))
        return user_guess
    
    def compare_answer(self, player_guess):
        if player_guess == self.answer:
            print(f"Congrats brother/sister! {player_guess} was the number! You win absolutely nothing.")
            return True
        elif player_guess > self.answer:
            print(f"Oof, {player_guess} is a little too large there big dog. Try again: ")
        else:
            print(f"You gotta go bigger than {player_guess} gamer. Guess again: ")


random_answer = random.randint(1, 100)

game = GuessingGame(random_answer)

user_guess = game.guess()

game.compare_answer(user_guess)

while True:
    user_guess = game.guess()
    if game.compare_answer(user_guess):
        break