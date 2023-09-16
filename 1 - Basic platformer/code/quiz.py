import pygame
pygame.init()
window_size = (700,500)
wind = pygame.display.set_mode(window_size)
pygame.display.set_caption("Coding Question")

button_color = (255, 255, 255)
button_rect = pygame.Rect(300, 250, 200, 100)
button_font = pygame.font.SysFont(None, 36)
button_text = button_font.render("Submit!", True, (0, 0, 0))
button_text_rect = button_text.get_rect(center=button_rect.center)
