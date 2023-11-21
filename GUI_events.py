import pygame


def rectangle_click(rectangle: pygame.rect):
    pos = pygame.mouse.get_pos()
    if pos[0] > rectangle.x and pos[0] < (rectangle.x + rectangle.width):
        if pos[1] > rectangle.y and pos[1] < (rectangle.y + rectangle.height):
            return True
    return False


def draw_text_button(window: pygame.display, button: pygame.rect, button_color: pygame.color, text: str,
                     text_color: pygame.color, font: pygame.font):
    pygame.draw.rect(window, button_color, button)
    button_text = font.render(text, True, text_color)
    text_rect = button_text.get_rect(center = button.center)
    window.blit(button_text, text_rect)

