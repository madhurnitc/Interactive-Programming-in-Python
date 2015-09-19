__author__ = 'Madhur'

# This program can be run directly in CodeSkulptor Environment By clicking this link below
# http://www.codeskulptor.org/#user40_oBfjn9jP5_17G.py


# template for "Stopwatch: The Game"
import simplegui
# define global variables
time = 0
a = 0
b = 0
c = 0
d = 0
total_stops = 0
successful_stops = 0
watch_running =  False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time,a,b,c,d
    a = t // 600
    b = ((t // 10) % 60) // 10
    c = ((t // 10) % 60) % 10
    d = t % 10
    return str(a) + ":" + str(b) + str(c) + "." + str(d)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global watch_running
    timer.start()
    watch_running =  True

def stop():
    global d , total_stops,successful_stops,watch_running
    timer.stop()
    if watch_running :
        watch_running = False
        total_stops += 1
        if int(d) == 0 :
            successful_stops += 1
        

def reset():
    global time,total_stops,successful_stops,watch_running
    timer.stop()
    time = 0
    total_stops = 0
    successful_stops = 0
    watch_running = False
    



# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1
    

# define draw handler
def drawhandler(canvas):
    global total_stops,successful_stops
    canvas.draw_text( str(successful_stops) + "/" + str(total_stops),[300,50],40,"Red")
    canvas.draw_text(str(format(time)),[160,200],40,"Green")
    
# create frame
frame = simplegui.create_frame("Stop Watch",400,400)
frame.set_draw_handler(drawhandler)
timer = simplegui.create_timer(100,timer_handler)
# register event handlers
frame.add_button("Start",start,100)
frame.add_button("Stop",stop,100)
frame.add_button("Reset",reset,100)


# start frame
frame.start()


# Please remember to review the grading rubric
