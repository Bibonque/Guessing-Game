<!-- # Build a Simple Guessing Game

Let's create a simple guessing game.

Your `GuessingGame` class should be initialized with an integer called something like `answer` or `answer_number`.

Define an instance method `GuessingGame#guess` (hashtags in documentation generally means it is a method. In our case, `GuessingGame` has a method called `guess`) which takes an integer called `user_guess` as its input. `#guess` should return the string `high` if the `user_guess` is larger than the `answer`, `correct` if the `user_guess` is equal to the `answer`, and `low` if the `user_guess` is lower than the `answer`.

Define an instance method `GuessingGame#solved` which returns `True` if the most recent `user_guess` was correct and `False` otherwise.

For example:

```python
# Define your GuessingGame class here...


game = GuessingGame(10)

game.solved()   # => False

game.guess(5)  # => 'low'
game.guess(20) # => 'high'
game.solved()   # => False

game.guess(10) # => 'correct'
game.solved()   # => True
```

Or:

```python
import random

# Define your GuessingGame class here...


# ----- main.py -----
game = GuessingGame(random.randint(1,100))
last_guess  = None
last_result = None

while game.solved() == False:
  if last_guess != None: 
    print(f"Oops! Your last guess ({last_guess}) was {last_result}.")
    print("")

  last_guess  = input("Enter your guess: ")
  last_result = game.guess(last_guess)


print(f"{last_guess} was correct!")
``` -->



import random

class GuessingGame():
    def __init__(self, answer):
        self.answer = answer
        print(f"I'm thinking of a number between 1 and 100. Can you guess it?")
    
    def guess(self):
        user_guess = int(input("Enter your guess: "))
        return user_guess

    def compare_answer(self, player_guess):
        if player_guess == self.answer:
            print(f"Congratulations! {player_guess} is correct. You win!")
        elif player_guess > self.answer:
            print(f"Too high! {player_guess} is larger than the correct answer.")
        else:
            print(f"Too low! {player_guess} is smaller than the correct answer.")

# Generate a random answer for the game
random_answer = random.randint(1, 100)

# Create an instance of the GuessingGame with the random answer
game = GuessingGame(random_answer)

# Allow the player to make a guess
user_guess = game.guess()

# Compare the user's guess with the answer
game.compare_answer(user_guess)
