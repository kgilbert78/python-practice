from graphics import GraphWin, Point
from button import Button

def main():
    win = GraphWin("Dice Roller")
    win.setCoords(0, 0, 10, 10)
    win.setBackground("green2")

    rollButton = Button(win, Point(5, 4.5), 6, 1, "Roll Dice")
    rollButton.activate()

    quitButton = Button(win, Point(5, 1,), 2, 1, "Quit")

    # pause to view window ( or to view until clicked anywhere, replace with win.getMouse() )
    input("Press <Enter> to quit.")

    win.close()

if __name__ == '__main__':
    main()