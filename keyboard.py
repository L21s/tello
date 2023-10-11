import pygame


def init():
    pygame.init()
    display_config = pygame.display.set_mode((400, 400))


def get_key(key):
    result = False
    for event in pygame.event.get():
        pass
    input_key = pygame.key.get_pressed()
    keyname = getattr(pygame, 'K_{}'.format(key))
    if input_key[keyname]:
        result = True
    pygame.display.update()
    return result


def main():
    if get_key("LEFT"):
        print("LEFT")
    if get_key("RIGHT"):
        print("RIGHT")
    if get_key("UP"):
        print("UP")
    if get_key("DOWN"):
        print("DOWN")


if __name__ == '__main__':
    init()
    while True:
        main()
