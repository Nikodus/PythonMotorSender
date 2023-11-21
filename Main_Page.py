import pygame
import Connection
import GUI_events
from GUI_colors import *
import sys



class Main_Page:

    def __init__(self):

        self.text_input = []
        self.connection_button = pygame.Rect(150, 50, 300, 50)
        self.motor_on_button = pygame.Rect(100, 150, 100, 50)
        self.motor_off_button = pygame.Rect(400, 150, 100, 50)
        self.select_motor = pygame.Rect(250, 150, 100, 50)
        self.set_button = pygame.Rect(130, 375, 140, 50)
        self.switch_to_controls = pygame.Rect(350, 375, 140, 50)
        self.text_field = pygame.Rect(210, 250, 180, 50)
        self.selected_motor = 0

    def main_page(self, window: pygame.display, conn: Connection.Connection):

        text_input = self.text_input
        connection_button = self.connection_button
        motor_on_button = self.motor_on_button
        motor_off_button = self.motor_off_button
        set_button = self.set_button
        text_field = self.text_field
        select_motor = self.select_motor
        switch_to_controls = self.switch_to_controls
        active_page = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                left, middle, right = pygame.mouse.get_pressed()
                if left:
                    if GUI_events.rectangle_click(connection_button):
                        conn.connect()
                    if GUI_events.rectangle_click(motor_on_button):
                        conn.send("MOTOR_ON")
                    if GUI_events.rectangle_click(motor_off_button):
                        conn.send("MOTOR_OFF")
                    if GUI_events.rectangle_click(set_button):
                        conn.send("MOTOR_DUTY_" + ''.join(text_input))
                        text_input.clear()
                    if GUI_events.rectangle_click(switch_to_controls):
                        active_page = 1
                    if GUI_events.rectangle_click(select_motor):
                        if conn.getMotorindex() == 1:
                            conn.setMotorindex(0)
                        elif conn.getMotorindex() == 0:
                            conn.setMotorindex(1)

            if event.type == pygame.KEYDOWN:
                text = event.unicode
                if text.isnumeric():
                    if len(text_input) < 5:
                        text_input.append(text)
                if text == "\x08":
                    try:
                        text_input.pop()
                    except:
                        None
                if text == "\r":
                    if len(text_input) == 0:
                        text_input.append("0")
                    conn.send("MOTOR_DUTY_" + ''.join(text_input))
                    text_input.clear()

        window.fill(color=background)

        if conn.isConnected():
            GUI_events.draw_text_button(window, connection_button, green, "Connection ON", white,
                                        small_text_font)
        else:
            GUI_events.draw_text_button(window, connection_button, red, "Connection OFF", white,
                                        small_text_font)

        if conn.getMotorindex() == 0:
            GUI_events.draw_text_button(window, select_motor, gray, "Motor 1", white,
                                        small_text_font)
        elif conn.getMotorindex() == 1:
            GUI_events.draw_text_button(window, select_motor, gray, "Motor 2", white,
                                        small_text_font)

        GUI_events.draw_text_button(window, switch_to_controls, gray, "Controls", white,
                                    small_text_font)

        GUI_events.draw_text_button(window, motor_on_button, gray, "Motor ON", white,
                                    small_text_font)
        GUI_events.draw_text_button(window, motor_off_button, gray, "Motor OFF", white,
                                    small_text_font)
        GUI_events.draw_text_button(window, set_button, gray, "Send", white, small_text_font)
        GUI_events.draw_text_button(window, text_field, light_gray, ''.join(text_input), black, text_font)

        return active_page
