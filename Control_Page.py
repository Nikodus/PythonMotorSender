import pygame
import Connection
import GUI_events
from GUI_colors import *
import sys


class Control_Page:

    def __init__(self):
        self.switch_to_Main_Page = pygame.Rect(350, 375, 140, 50)
        self.connection_button = pygame.Rect(150, 50, 300, 50)
        self.forward_button = pygame.Rect(250, 130, 70, 70)
        self.reverse_button = pygame.Rect(250, 320, 70, 70)
        self.left_button = pygame.Rect(150, 225, 70, 70)
        self.right_button = pygame.Rect(350, 225, 70, 70)
        self.stop_button = pygame.Rect(250, 225, 70, 70)

    def control_page(self, window: pygame.display, conn: Connection.Connection):
        switch_to_main_page = self.switch_to_Main_Page
        connection_button = self.connection_button
        forward_button = self.forward_button
        reverse_button = self.reverse_button
        left_button = self.left_button
        right_button = self.right_button
        stop_button = self.stop_button
        active_page = 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                left, middle, right = pygame.mouse.get_pressed()
                if left:
                    if GUI_events.rectangle_click(switch_to_main_page):
                        active_page = 0
                    if GUI_events.rectangle_click(connection_button):
                        if conn.isConnected():
                            conn.disconnect()
                        else:
                            conn.connect()
                    if GUI_events.rectangle_click(forward_button):
                        conn.setMotorindex(0)
                        conn.send("MOTOR_DUTY_1000")
                        conn.setMotorindex(1)
                        conn.send("MOTOR_DUTY_1000")

                    if GUI_events.rectangle_click(right_button):
                        conn.setMotorindex(0)
                        conn.send("MOTOR_DUTY_1000")
                        conn.setMotorindex(1)
                        conn.send("MOTOR_DUTY_0")

                    if GUI_events.rectangle_click(left_button):
                        conn.setMotorindex(0)
                        conn.send("MOTOR_DUTY_0")
                        conn.setMotorindex(1)
                        conn.send("MOTOR_DUTY_1000")

                    if GUI_events.rectangle_click(stop_button):
                        conn.setMotorindex(0)
                        conn.send("MOTOR_DUTY_0")
                        conn.setMotorindex(1)
                        conn.send("MOTOR_DUTY_0")



        window.fill(color=background)

        if conn.isConnected():
            GUI_events.draw_text_button(window, connection_button, green, "Connection ON", white,
                                        small_text_font)
        else:
            GUI_events.draw_text_button(window, connection_button, red, "Connection OFF", white,
                                        small_text_font)

        GUI_events.draw_text_button(window, switch_to_main_page, gray, "Motor Test", white,
                                    small_text_font)

        GUI_events.draw_text_button(window, forward_button, gray, "FW", white, medium_text_font)
        GUI_events.draw_text_button(window, reverse_button, gray, "REV", white, medium_text_font)
        GUI_events.draw_text_button(window, left_button, gray, "LEFT", white, medium_text_font)
        GUI_events.draw_text_button(window, right_button, gray, "RIGHT", white, medium_text_font)
        GUI_events.draw_text_button(window, stop_button, red, "STOP", white, medium_text_font)

        return active_page
