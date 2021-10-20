from os import X_OK
from pico2d import *

# Game object class here
class JPmap:               #점핑맵 로드
    def __init__(self):
        self.image=load_image('jumping.png')
    pass
    
    def draw(self):
        self.image.draw(70,350)
    pass

class Mario:    #이미지 위치 속성을 만들어줘야돼
    def __init__(self):
        self.image = load_image('run_mario.png')
        self.x ,self.y,=20,40
        self.running,self.dir=True,0
        self.frame = 0
       
    def handle_events(self):
    
        for event in get_events():
            if event.type == SDL_QUIT:
                self.running = False
            elif event.type ==SDL_KEYDOWN:
                if event.key==SDLK_RIGHT:
                    self.dir += 1
                elif event.key==SDLK_LEFT:
                    self.dir -= 1
            elif event.type==SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    self.dir -= 1
                elif event.key == SDLK_LEFT:
                    self.dir += 1
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                self.running = False

    def update(self):  #마리오의 행위 구현.
        self.x +=dir*5    #속성값을 바꿈으로써, 행위를 구현
        self.x +=1
    def draw(self):
        self.frame =(self.frame+1)%3
        self.image.clip_draw(self.frame*30,0,40,73,self.x,self.y)



# initialization code
open_canvas(70,600)

jpmap = JPmap() #점핑맵 객체 생성
mario = Mario()
running = True
# game main loop code
while True:
   
    #Game logic
    # mario.update()  #마리오의 상호작용 
 
     
    #Game drawing 
    clear_canvas()
    jpmap.draw()
    mario.draw()
    mario.handle_events()
    update_canvas()

    
    delay(0.05)

    
    
    


close_canvas()
# finalization code

