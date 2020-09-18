from pico2d import *
import os

os.chdir('C:/Users/이도영/Desktop/수업 2-2/2D겜플/2DGP_03/res')

open_canvas()

img = load_image('run_animation.png')
gra = load_image('grass.png')


frame = 0
for x in range(0,800,2):
    clear_canvas()
    
    gra.draw(400,30)
    img.clip_draw(frame* 100, 0, 100, 100, x, 80)

    update_canvas()

    frame  = (frame +1 ) %8

    get_events()
    delay(0.01)
    

delay(5)
close_canvas()





























