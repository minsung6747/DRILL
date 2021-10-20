import random 
from pico2d import *

# Game object class here
class Grass:
    def __init__ (self):
        self.image=load_image('grass.png')
    
    def draw(self):
        self.image.draw(400,30)
    pass

 #Grass 라는 클래스로부터, grass 객체를 생성한다.
class sBall:
    def __init__(self):
        self.image=load_image('ball21x21.png')
        self.x,self.y=random.randint(100,700),500

    def update(self):
        self.y -= random.randint(1,6)
            
            
    def draw(self):
        self.image.draw(self.x,self.y)
    
class bBall:
    def __init__(self):
        self.image=load_image('ball41x41.png')
        self.x,self.y=random.randint(100,700),500
    
    def update(self):
        self.y -= random.randint(1,6)
        
    def draw(self):
        self.image.draw(self.x,self.y)    

class Boy:
    def __init__(self):
        self.image=load_image('run_animation.png')
        self.x,self.y=random.randint(100,700),90
        self.frame=0
    
    def update(self):
        self.x += 5
        self.frame = (self.frame+1) % 8
    def draw(self):
        self.image.clip_draw(self.frame*100,0,100,100,self.x,self.y)

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

# initialization code
open_canvas()

grass = Grass()
# boy = Boy()
sball=sBall()
bball=bBall()
team =[Boy() for i in range(11)]
things=[sBall() for i in range(20)]
things2=[bBall() for i in range(20)]
running=True
# game main loop code

while running:

    handle_events()
       #소년의 상태 업그레이드
    for boy in team:
        boy.update()
        
    for sball in things:
        sball.update()
    
    for bball in things2:
        bball.update()
    
    clear_canvas()
    
    grass.draw()
    for boy in team:
        boy.draw()    
    
    for sball in things:
        sball.draw()

    for bball in things2:
        bball.draw()
    

    
    update_canvas()

    delay(0.05)
# finalization code