from pico2d import*

open_canvas()
import os

os.getcwd()
os.chdir('C:/Users/이도영/Desktop/수업 2-2/2D겜플/2DGP_03/res')
os.listdir()
image = load_image('character.png')
image.draw_now(500,200)
delay(2)
close_canvas()
