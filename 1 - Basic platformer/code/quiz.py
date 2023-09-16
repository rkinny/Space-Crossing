import pygame
import random
import json

pygame.init()
 
#available colors
white = (255, 255, 255)
black = (0,0,0)
 
# assigning values to X and Y variable
width = 800
height = 600

display_surface = pygame.display.set_mode((width, height))
pygame.display.set_caption('Show Text')
font = pygame.font.Font('freesansbold.ttf', 16)
 
#question
questions = json.load(open("questions.json"))
question = random.choice(list(questions.keys()))
answer = questions[question]['answer']
text = font.render(question, True, white, black)

base_font = pygame.font.Font(None, 32)
user_input = ''
input_rect = pygame.Rect(height//2, width//2, 140, 32)
typing_color = pygame.Color('gray')
idle_color = pygame.Color('white')
color = idle_color

typing = False
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (width // 2, height // 4)

# infinite loop
while True:
    display_surface.fill(black)
    display_surface.blit(text, textRect)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                typing = True
            else:
                typing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                user_input = user_input[:-1]
            else:
                user_input += event.unicode
        if typing:
            color = typing_color
        else:
            color = idle_color
    pygame.draw.rect(display_surface, color, input_rect)
    text_surface = base_font.render(user_input, True, (255, 255, 255))
    display_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
    input_rect.w = max(100, text_surface.get_width()+10)
    pygame.display.flip()
    pygame.display.update()
pygame.quit()