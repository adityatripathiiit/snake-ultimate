#########################################################
# RUN 'snakegame.py' TO STATR THE GAME FROM THE STATING #
#########################################################

#########################################################
# THIS IS NOT TO BE RUN, FROM HERE ######################
#########################################################


import turtle
import time
def face1():
    import main
    execfile('main.py')
def face2():
    import main2
    execfile('main2.py')
display = turtle.Screen()
display.title("Snake Ultimate by ADITYA and DEVANSHU")
display.bgpic('Images\\head_select.gif')
display.setup(width=600, height=600)
display.tracer(0) # Turns off the screen updates
display.listen()
display.onkeypress(face1, "1")
display.onkeypress(face2,"2")
display.mainloop()