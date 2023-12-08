from GameEngine import GameEngine


def main():
    x = GameEngine()
    x.initializeGame()
    x.intro()
    print(f"{x.remainingVeggies()} veggies remaining. Current score: {x.getScore()}")
    x.printField()
    while x.remainingVeggies() != 0:
        x.moveCaptain()
        print(f"{x.remainingVeggies()} veggies remaining. Current score: {x.getScore()}")
        x.printField()
    x.gameOver()
    x.highScore()


main()
