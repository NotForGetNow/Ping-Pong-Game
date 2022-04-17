from pygame import * 
 
class GameSprite(sprite.Sprite): 
    def __init__(self, p_image, p_x, p_y, p_speed, w, h): 
        super().__init__() 
        self.image = transform.scale(image.load(p_image), (w, h)) 
        self.speed = p_speed 
        self.rect = self.image.get_rect() 
        self.rect.x = p_x 
        self.rect.y = p_y 
    def reset(self): 
        window.blit(self.image, (self.rect.x, self.rect.y)) 
 
class Player(GameSprite): 
    def right_update(self): 
        keys = key.get_pressed() 
        if keys[K_UP] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < w_h - 80: 
            self.rect.y += self.speed 
    def left_update(self): 
        keys = key.get_pressed() 
        if keys[K_w] and self.rect.y > 5: 
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < w_h - 80: 
            self.rect.y += self.speed 
 
bg = (200, 255, 255) #background
w_w = 600 #win width
w_h = 500 #win height
window = display.set_mode((w_w, w_h)) 
window.fill(bg) 
 
game = True 
finish = False 
clock = time.Clock() 
FPS = 60 

racket_l = Player('***', 520, 200, 4, 50, 50)
racket_r = Player('***', 30, 200, 4, 50, 150) 
ball = GameSprite('***', 200, 200, 4, 50, 50)

font.init()
font = font.Font(Arial, 35)

lose1 = font.render('P1 LOSE!', True, (180, 0, 0))
lose2 = font.render('P2 LOSE!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        window.fill(bg)
        racket_l.left_update()
        racket_r.right_update()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        if sprite.collide_rect(racket_l) or sprite.collide_rect(racket_r):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > w_h - 50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game = True

        if ball.rect.y > w_w:
            finish = True
            window.blit(lose2, (200, 200))
            game = True

        racketl.reset()
        racketr.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)