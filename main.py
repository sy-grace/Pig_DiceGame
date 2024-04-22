import random

def roll():
    return random.randint(1, 7)

def turn(player, total_score, target):
    print(f"{player}'s turn!")
    score = 0
    while True:
        dice = roll()
        print(f"You rolled {dice}")
        if dice == 1:
            print("You rolled 1. Bummer:(")
            return 0
        score += dice
        print(f"Your score is {total_score + score}")

        if score + total_score >= target:
            return score

        bank = input("Do you want to store the score and end your turn? (Y/N): ")
        if bank.lower() == 'y':
            return score
    

def game(target):
    p1 = 0
    p2 = 0
    while True:
        p1 += turn("Player 1", p1, target)
        print(f"Player 1's total score: {p1}\n")
        if p1 > target:
            print("\nPlayer 1 win!")
            break

        p2 += turn("Player 2", p2, target)
        print(f"Player 2's total score: {p2}\n")
        if p2 > target:
            print("\nPlayer 2 win!")
            break
        

if __name__ == '__main__':
    print("New Game!")
    target = int(input("Select your target score (50 or 100): "))
    game(target)
