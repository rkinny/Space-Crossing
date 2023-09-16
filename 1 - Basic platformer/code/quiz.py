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
 
# create a font object.
# 1st parameter is the font file
# which is present in pygame.
# 2nd parameter is size of the font
font = pygame.font.Font('freesansbold.ttf', 16)
 
#question
questions = json.load(open("questions.json"))
question = random.choice(list(questions.keys()))
answer = questions[question]['answer']
text = font.render(question, True, white, black)

base_font = pygame.font.Font(None, 32)
user_text = ''
  
# create rectangle
input_rect = pygame.Rect(height//2, width//2, 140, 32)
  
# color_active stores color(lightskyblue3) which
# gets active when input box is clicked by user
color_active = pygame.Color('gray')
  
# color_passive store color(chartreuse4) which is
# color of input box.
color_passive = pygame.Color('white')
color = color_passive
  
active = False
#text rect
textRect = text.get_rect()
 
# set the center of the rectangular object.
textRect.center = (width // 2, height // 4)

button_color = (255, 255, 255)
button_rect = pygame.Rect(300, 250, 200, 100)
button_font = pygame.font.SysFont(None, 36)
button_text = button_font.render("Submit!", True, (0, 0, 0))
button_text_rect = button_text.get_rect(center=button_rect.center)
# infinite loop
while True:
 
    # completely fill the surface object
    # with black color
    display_surface.fill(black)
 
    # copying the text surface object
    # to the display surface object
    # at the center coordinate.
    display_surface.blit(text, textRect)
 
    # iterate over the list of Event objects
    # that was returned by pygame.event.get() method.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False
  
        if event.type == pygame.KEYDOWN:
  
            # Check for backspace
            if event.key == pygame.K_BACKSPACE:
  
                # get text input from 0 to -1 i.e. end.
                user_text = user_text[:-1]
  
            # Unicode standard is used for string
            # formation
            else:
                user_text += event.unicode
        # Draws the surface object to the screen.
        if active:
            color = color_active
        else:
            color = color_passive
          
    # draw rectangle and argument passed which should
    # be on screen
    pygame.draw.rect(display_surface, color, input_rect)
  
    text_surface = base_font.render(user_text, True, (255, 255, 255))
      
    # render at position stated in arguments
    display_surface.blit(text_surface, (input_rect.x+5, input_rect.y+5))
      
    # set width of textfield so that text cannot get
    # outside of user's text input
    input_rect.w = max(100, text_surface.get_width()+10)
      
    # display.flip() will update only a portion of the
    # screen to updated, not full area
    pygame.display.flip()
    pygame.display.update()
pygame.quit()