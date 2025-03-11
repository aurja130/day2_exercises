from .die import Die

class DiceGame:

    def __init__(self):
        number_of_dice = 5
        self.dice = [Die() for _ in range(number_of_dice)]
        self.reset()

    def reset(self):
        self.round = 0
        self.wins = 0
        self.losses = 0

    def answer(self):
        total = 0
        for die in self.dice:
            total += die.value
        return total

    def run(self):
        
        while True:

            self.round += 1

            print(f'Round {self.round}\n')

            for die in self.dice:
                die.roll()
                print(die.top_surface())

            total = self.answer()

            guess = input("Alright, what is your guess?: ")
            guess = int(guess)

            if guess == total:
                print("Correct!")
                self.wins += 1
            else:
                print("")
                print(f'Sorry, that is wrong. The answer is {total}.')
                self.losses += 1
            print(f"Wins: {self.wins}, Losses: {self.losses}.")

            if self.round == 5:
                if self.wins > self.losses:
                    print("You won! Congrats!")
                else:
                    print("You lost! Better luck next time!")
                break

            prompt = input("Would you like to play again?[y/n]: ")

            if prompt == 'y':
                print("Yay, let's go!")
                continue
            elif prompt == 'n':
                print("You're a quitter!")
                break
            else:
                raise Exception("Invalid input :(")
                break
