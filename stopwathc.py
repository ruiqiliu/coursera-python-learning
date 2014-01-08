import simpleguitk as simplegui
import random
import math

time = 0 
message = "0:00.0"
success = 0 
total = 0
def forBC(t):
    if t < 10 :
        return "0" + str(t)
    else:
        return str(t)
def format(t):
    """ covert int to string a:bc:d """
    a = t // 600 
    t = t - a * 600 
    b = t // 10 
    d = t % 10 
    return str(a)+":"+forBC(b)+"."+str(d) 

#define event handler for buttons: start stop reset    
def start():
    timer.start()

def stop():    
    global success, total 
    if timer.is_running():
        timer.stop()
        total += 1 
        if (time % 10 == 0) :
           success += 1 
def reset():
    global time, message,success, total 
    timer.stop()
    time = 0
    success = 0; total = 0
    message = format(time)
def timer_handler():
    global time, message
    time += 1 
    message = format(time )
def draw_handler(canvas):
    canvas.draw_text(message, [20, 122], 40, "Red")
    canvas.draw_text(str(success)+"/"+str(total),[120,60],30,"Green")

frame = simplegui.create_frame("Stop Watch", 200, 200)
frame.add_button("start", start)
frame.add_button("stop", stop)
frame.add_button("reset",reset)
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)

frame.start()

