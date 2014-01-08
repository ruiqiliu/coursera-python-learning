import simpleguitk as simplegui
import random
import math

#initialize globals - pos and vel 
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2

#CONSTATS FOR RANDOM VELOCITY GENERATION
#VSCALE = 2
#VOFFSETX = 2
#VOFFSETY = 0.5

#global ball pos vel 
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_velx = 2
ball_vely = 1
paddle1_pos = HEIGHT / 2
paddle2_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_vel = 0
PAD_VEL = 3
score1 = 0
score2 = 0 
#helper function
def spawn_ball():
    global ball_pos , ball_velx, ball_vely , score1, score2
    ball_pos[0] += ball_velx
    ball_pos[1] += ball_vely
    
    #chech the wall and chage velocity
    if ball_pos[0] <= BALL_RADIUS or ball_pos[0] >= WIDTH - BALL_RADIUS:
        ball_velx = -ball_velx
    if ball_pos[1] <= BALL_RADIUS or ball_pos[1] >= HEIGHT - BALL_RADIUS:
        ball_vely = -ball_vely

    #check the ball and paddle
    if ball_pos[0] <= BALL_RADIUS :
        if ball_pos[1] < paddle1_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle1_pos + HALF_PAD_HEIGHT:
            score2 += 1 
        else:    
            increase_ball_vel()
    if ball_pos[0] >= WIDTH - BALL_RADIUS :
        if ball_pos[1] < paddle2_pos - HALF_PAD_HEIGHT or ball_pos[1] > paddle2_pos + HALF_PAD_HEIGHT:
            score1 += 1 
        else:     
            increase_ball_vel()

def increase_ball_vel():
    global ball_velx, ball_vely, paddle1_vel,paddle2_vel,PAD_VEL
    if abs(ball_velx) > 8:
        return 
    PAD_VEL *= 1.2
    ball_velx *= 1.2
    ball_vely *= 1.1

#define event handlers
def new_game():
    global paddle1_pos,paddle2_pos,paddle1_vel,paddle2_vel
    global score1,score2, ball_pos , ball_velx, ball_vely ,PAD_VEL
    #reset ball
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    ball_velx = random.randrange(-5,5); ball_vely = random.randrange(-4,4) 
    if ball_velx == 0 or ball_vely == 0 :
        ball_velx = 2
        ball_vely = 1

    #score to 0
    score1 = score2 = 0 
    #reset pad_vel
    PAD_VEL = 3 


def draw(c):
    global score1,score2,paddle2_pos,paddle1_pos,ball_vel,PAD_VEL

    #draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1 , "White")

    #update ball
    spawn_ball()
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "Yellow", "White") 

    #update paddle`s vertical position, keep paddle on the screen
    paddle1_pos += paddle1_vel
    paddle2_pos += paddle2_vel 
    if paddle1_pos <=  HALF_PAD_HEIGHT:
        paddle1_pos =  HALF_PAD_HEIGHT
    if paddle2_pos <=  HALF_PAD_HEIGHT:    
        paddle2_pos =  HALF_PAD_HEIGHT

    if paddle1_pos >= HEIGHT - HALF_PAD_HEIGHT :
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    if paddle2_pos >= HEIGHT - HALF_PAD_HEIGHT:    
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
        
    #draw paddles
    c.draw_polygon([(0,paddle1_pos - HALF_PAD_HEIGHT),(PAD_WIDTH, paddle1_pos - HALF_PAD_HEIGHT),
        (PAD_WIDTH, paddle1_pos + HALF_PAD_HEIGHT),(0, paddle1_pos + HALF_PAD_HEIGHT)],1, 'White','White')
    c.draw_polygon([(WIDTH - PAD_WIDTH,paddle2_pos - HALF_PAD_HEIGHT),(WIDTH, paddle2_pos - HALF_PAD_HEIGHT),
        (WIDTH, paddle2_pos + HALF_PAD_HEIGHT),(WIDTH - PAD_WIDTH, paddle2_pos + HALF_PAD_HEIGHT)],1, 'White','White')

    #draw scores
    c.draw_text(score1 , (WIDTH / 2 - 50, 50), 32, "Red")
    c.draw_text(score2 , (WIDTH / 2 + 50, 50), 32, "Red")

def keydown(key):
    global paddle1_vel,paddle2_vel
    if key == simplegui.KEY_MAP['w']:
        paddle1_vel = -PAD_VEL
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = PAD_VEL

    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -PAD_VEL
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = PAD_VEL
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel  = paddle2_vel = 0

frame = simplegui.create_frame("Ping pong", WIDTH, HEIGHT)
frame.add_button("Restart", new_game,50)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

frame.start()
