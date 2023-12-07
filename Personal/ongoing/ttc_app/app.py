import pygame as pg
import sys
pg.init()

# Set up display
width, height = 450, 800
screen = pg.display.set_mode((width, height))
clock = pg.time.Clock()
pg.display.set_caption("Text Box Example")

#for the text box
font = pg.font.Font(None, 20)

#function creates a text box and returns whatever is typed in, and a bool repersenting if the enter button has been pressed
#event is a list of all events that happened during this frame
def create_text_box(event, location, size, text, color=(0,0,0) ):
    x,y = location
    width,height = size
    for event in events:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN: return text, True
            elif event.key == pg.K_BACKSPACE: text = text[:-1]
            elif event.unicode: text += event.unicode
    pg.draw.rect(screen, color, (x, y, width, height), 2)
    text_box = font.render(text, True, color)
    screen.blit(text_box, (x + 5, y + 5))
    return text, False

def reporting_screen(event, station_text, description_text):
    station_text, enter_pressed = create_text_box(event, (100, 100), (200, 40), station_text)
    if enter_pressed:
        print(station_text)
        station_text=''
    return station_text
report_station_text = ''
while True:
    screen.fill((255,255,255))
    events = pg.event.get()
    for event in events:
        if event.type == pg.QUIT:
            break

    report_station_text = reporting_screen(event, report_station_text, "hihihi")
    pg.display.update()

pg.quit()
sys.exit()