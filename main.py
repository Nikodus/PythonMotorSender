from Connection import Connection as Conn
import pygame
from Main_Page import Main_Page
from Control_Page import Control_Page

conn = Conn("192.168.1.104",7777)

pygame.init()
size = width, height = 600, 480
active_page = 0
window = pygame.display.set_mode(size)

main_page = Main_Page()
control_page = Control_Page()

while True:

    if active_page == 0:
        active_page = main_page.main_page(window,conn)
    elif active_page == 1:
        active_page = control_page.control_page(window,conn)


    pygame.display.update()



