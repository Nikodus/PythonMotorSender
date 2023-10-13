import pygame


def rectangle_click(rectangle: pygame.rect):
    pos = pygame.mouse.get_pos()
    if pos[0] > rectangle.x and pos[0] < (rectangle.x + rectangle.width):
        if pos[1] > rectangle.y and pos[1] < (rectangle.y + rectangle.height):
            return True
    return False