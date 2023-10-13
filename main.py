from Connection import Connection as Conn
import pygame
import sys
import GUI_events


conn = Conn()

pygame.init()
size = width, height = 600, 480
window = pygame.display.set_mode(size)


text_font = pygame.font.Font(None,64)
small_text_font = pygame.font.Font(None,24)
text_input = []

connection_button = pygame.Rect(150,50,300,50)
motor_on_button = pygame.Rect(100,150,100,50)
motor_off_button = pygame.Rect(400,150,100,50)
set_button = pygame.Rect(230,350,140,50)
text_field = pygame.Rect(210,250,180,50)



while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            left,middle,right = pygame.mouse.get_pressed()
            if left:
                if GUI_events.rectangle_click(connection_button):
                    conn.connect()
                if GUI_events.rectangle_click(motor_on_button):
                    conn.send("MOTOR_ON")
                if GUI_events.rectangle_click(motor_off_button):
                    conn.send("MOTOR_OFF")
                if GUI_events.rectangle_click(set_button):
                    conn.send("MOTOR_DUTY_"+' '.join(text_input))
                    text_input.clear()

        if event.type == pygame.KEYDOWN:
            text = event.unicode
            if text.isnumeric():
                if len(text_input) <5:
                    text_input.append(text)
            if text == "\x08":
                text_input.pop()
            if text == "\r":
                text_input.clear()
                if conn.isConnected():
                    conn.send("MOTOR_DUTY_"+' '.join(text_input))



    window.fill(color=(40,40,40))

    if conn.isConnected():
        pygame.draw.rect(window, (0, 255, 0), connection_button)
    else:
        pygame.draw.rect(window, (255, 0, 0), connection_button)
    pygame.draw.rect(window, (150, 150, 150), motor_on_button)
    pygame.draw.rect(window, (150, 150, 150), motor_off_button)
    pygame.draw.rect(window, (150, 150, 150), set_button)
    pygame.draw.rect(window, (200, 200, 200), text_field)

    text_for_input = text_font.render(' '.join(text_input),True,(255,255,255))
    text_motor_on_info = small_text_font.render("Motor On",True,(255,255,255))
    text_motor_off_info = small_text_font.render("Motor OFF", True, (255, 255, 255))
    text_connection_on = text_font.render("Connection ON", True, (255, 255, 255))
    text_connection_off = small_text_font.render("Connection OFF", True, (255, 255, 255))
    text_send = small_text_font.render("Send", True, (255, 255, 255))

    window.blit(text_for_input,(210,250))
    window.blit(text_motor_on_info, (115, 165))
    window.blit(text_motor_off_info, (410, 165))
    window.blit(text_send, (275,365))
    if conn.isConnected():
        window.blit(text_connection_on, (230,65))
    else:
        window.blit(text_connection_off, (230, 65))




    pygame.display.update()

