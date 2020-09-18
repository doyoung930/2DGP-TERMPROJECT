Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from pico2d import*
Pico2d is prepared.
>>> open_canvas()
>>> import os
>>> os.chdir('C:/Users/이도영/Desktop/수업 2-2/2D겜플/2DGP_03')
]
>>> os.listir()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    os.listir()
AttributeError: module 'os' has no attribute 'listir'
>>> os.chdir('C:/Users/이도영/Desktop/수업 2-2/2D겜플/2DGP_03')
>>> os.listir()
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.listir()
AttributeError: module 'os' has no attribute 'listir'
>>> os.chdir('C:/Users/이도영/Desktop/수업 2-2/2D겜플/2DGP_03/res')
>>> os.listir()
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    os.listir()
AttributeError: module 'os' has no attribute 'listir'
>>> os.lisdir()
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    os.lisdir()
AttributeError: module 'os' has no attribute 'lisdir'
>>> os.listdir()
['animation_sheet.png', 'character.png', 'grass.png', 'run_animation.png']
>>> 
>>> image = load_image('character.png')
>>> for y in range(100, 501, 80):
	for x in range(100,701, 35):
		image.draw_now(x,y)

		
>>> open canvase()
SyntaxError: invalid syntax
>>> open_canvas()
>>> for y in range(100, 501, 80):
	for x in range(100,701, 35):
		image.draw_now(x,y)

		
>>> close_canvas()
>>> open_cnavas()
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    open_cnavas()
NameError: name 'open_cnavas' is not defined
>>> open_canvas()
>>> image = load_image('character.png')
>>> image.draw_now(300, 200)
>>> 
>>> for y in range(100, 501, 80):
	for x in range(100,701, 35):
		image.draw_now(x,y)

		
>>> os.getcwd()
'C:\\Users\\이도영\\Desktop\\수업 2-2\\2D겜플\\2DGP_03\\res'
>>> grass = load_image('grass.png)
		   
SyntaxError: EOL while scanning string literal
>>> grass = load_image('grass.png')
>>> grass.draw_now(