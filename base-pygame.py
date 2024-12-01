import pygame
from collections import namedtuple
from random import randint

pygame.init()

Color = namedtuple('Color', ['red', 'green', 'blue'])
Mode = namedtuple('Mode', ['width', 'height'])

BACKGROUND_COLOR = Color(36, 188, 168)
RECTANGE_COLOR = Color(255, 255, 255)
ORANGE_COLOR = Color(255, 132, 75)
CIRCLE_COLOR = Color(255, 253, 65)
BLACK_COLOR = Color(0, 0, 0)
WINDOW_MODE = Mode(620, 480)

screen = pygame.display.set_mode(WINDOW_MODE) # screen size.
caption = pygame.display.set_caption('PyGame') # title of displayed window.
screen.fill(BACKGROUND_COLOR) # to change background-color of displayed window. [RGB-A]

# uses to create font(шрифт) object
font = pygame.font.Font(None, 28) # args: (arg1: path to font file, arg2: size of font)

# if we want to calculate window size we can use:
screen.get_height() and screen.get_width()

# The Clock is going to let us limit how often the window gets painted, by setting a maximum frame rate
clock = pygame.time.Clock() 

def main():
    base_color = BACKGROUND_COLOR

    rect_size=50
    rect_position = [10, 10, rect_size, rect_size]
    rect_velocity = [randint(-5, 5), randint(-5, 5)]

    curcle_width = screen.get_width() // 2
    circle_height = screen.get_height() // 2
    position_circle = [curcle_width, circle_height]

    while True:
        for e in pygame.event.get():
            print(e)
            if e.type == pygame.QUIT:
                return
            elif e.type == pygame.MOUSEMOTION:
                position_circle = e.__dict__['pos'] # position of mouse

        screen.fill(base_color) # to change background-color of displayed window. [RGB-A]

        # rect in an func with allows to draw recrangle in our displayed window.
        # rect takes as an arguments: (any surface object, Color, positons: [x, y, rectWidht, rectHeight])
        pygame.draw.rect(screen, RECTANGE_COLOR, rect_position)

        # circle takes as an arguments: (any surface object, Color, positons: [x, y], radius)
        pygame.draw.circle(screen, CIRCLE_COLOR, position_circle, 10)

        text = font.render('PyGame', True, BLACK_COLOR) # (arg1: displated text: arg2: bool: anti-aliasing, arg3: Color)
        screen.blit(text, (curcle_width - 50, 10))
        pygame.display.update() # rerender display

        if rect_position[0] < 0:
            rect_velocity[0] = -rect_velocity[0]
            base_color = ORANGE_COLOR
        elif rect_position[0] + rect_size > screen.get_width():
            base_color= BACKGROUND_COLOR
            rect_velocity[0] = -rect_velocity[0]

        if rect_position[1] < 0:
            rect_velocity[1] = -rect_velocity[1]
            base_color= BACKGROUND_COLOR
        elif rect_position[1] + rect_size > screen.get_height():
            base_color = ORANGE_COLOR
            rect_velocity[1] = -rect_velocity[1]

        rect_position[0] += rect_velocity[0]
        rect_position[1] += rect_velocity[1]

        clock.tick(50) # (arg: FPS)


            
main()