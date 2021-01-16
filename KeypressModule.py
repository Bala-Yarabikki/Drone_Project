import pygame


def init():
    pygame.init()
    win = pygame.display.set_mode((400, 400))


def getkey(keyname):
    ans = False
    for eve in pygame.event.get(): pass
    # Capturing keyinput
    keyInput = pygame.key.get_pressed()
    # return pressed key in K_format
    myKey = getattr(pygame, "K_{}".format(keyname))
    # updating display with pressed key
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans


def main():
    if getkey("LEFT"):
        print("Left key pressed")
    if getkey("RIGHT"):
        print("Right key pressed")
    if getkey("UP"):
        print("Up key pressed")
    if getkey("DOWN"):
        print("Down key pressed")


if __name__ == "__main__":
    init()
    while True:
        main()