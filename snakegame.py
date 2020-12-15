# this file is used to diplay the window for selection of the head and quiting. This is the starting code


import turtle
import time
def Face_select():
	import Face_select
	execfile('Face_select.py')


def DONOTHING():
	display = turtle.Screen()
	display.clear()
	display.title("Snake Ultimate by ADITYA and DEVANSHU")
	display.bgpic('Images\\exit.gif')
	display.setup(width=600, height=600)
	time.sleep(3)	
	turtle.bye()
	
	

display = turtle.Screen()
display.title("Snake Ultimate by ADITYA and DEVANSHU")
display.bgpic('Images\\Home.gif')
display.setup(width=600, height=600)
display.tracer(0) # Turns off the screen updates
display.listen()
display.onkeypress(Face_select, "space")
display.onkeypress(DONOTHING,"q")
display.mainloop()