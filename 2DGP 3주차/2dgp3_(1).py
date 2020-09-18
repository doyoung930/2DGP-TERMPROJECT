from pico2d import *

def handle_events():
    global running
    evts = get_events()
    for e in evts:
        if e.type == SDL_QUIT:
            running = False
        elif e.type == SDL_KEYDOWN:
            if e.key == SDLK_ESCAPE:
                running = False

import os

os.chdir('C:/Users/이도영/Desktop/수업 2-2/2D겜플/2DGP_03/res')

open_canvas()

img = load_image('run_animation.png')
gra = load_image('grass.png')

running = True
x = 0
frame = 0
while running and x< 800:

    clear_canvas()
    
    gra.draw(400,30)
    img.clip_draw(frame* 100, 0, 100, 100, x, 80)

    update_canvas()

    x += 2
    frame  = (frame +1 ) % 8

    handle_events()

    delay(0.01)
    


close_canvas()






