import pygame as pg
import sys
pg.init()

def create_text_box(font, location, size, text, color, events):
    x,y = location
    width,height = size
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                return text, True
            elif event.key == pg.K_BACKSPACE:
                text = text[:-1]
            elif event.unicode:  # Add typed characters to the text
                text += event.unicode

    pg.draw.rect(screen, (255, 255, 255), (x, y, width, height))
    pg.draw.rect(screen, color, (x, y, width, height), 2)

    text_surface = font.render(text, True, color)
    screen.blit(text_surface, (x + 5, y + 5))
    return text, False

# Set up display
width, height = 800, 600
screen = pg.display.set_mode((width, height))
pg.display.set_caption("Text Box Example")
font = pg.font.Font(None, 36)
clock = pg.time.Clock()

input_text = ""
running = True

while running:
    screen.fill((255,255,255))

    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            running = False

    input_text, enter_pressed = create_text_box(font, (100, 100), (200, 40), input_text, (0,0,0), events)
    if enter_pressed:
        print(input_text)
        input_text=""
    pg.display.flip()
    clock.tick(30)

pg.quit()
sys.exit()
