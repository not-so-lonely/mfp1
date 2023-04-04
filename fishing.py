from pygame import*
import random as rd

clock = time.Clock()#часы для игры
FPS = 120


okno = display.set_mode((600, 700))

#fon0 = image.load('bg_sky.jpg')
fon1 = image.load("bcgd.jpg") 
fon2 = image.load("bcgd.jpg") 
fon3 = image.load("bcgd.jpg")
fon1 = transform.scale(fon1, (600, 700)) 
fon2 = transform.scale(fon2, (600, 700)) 
fon3 = transform.scale(fon3, (600, 700)) 
#fon0 = transform.scale(fon0, (600, 200))


class sprait(sprite.Sprite):
    def __init__(self, kartinka, x, y):
        super().__init__()
        self.image = transform.scale(image.load(kartinka), (50, 80))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))


class igrok(sprait):
    def upravl(self):
        self.ris()
        knopki = key.get_pressed()
        if knopki[K_RIGHT]:
            self.rect.x += 5
        if knopki[K_LEFT]:
            self.rect.x -= 5
        if knopki[K_UP] and self.rect.y >= -10:
            self.rect.y -= 5
        if knopki[K_DOWN] and self.rect.y <= 300:
            self.rect.y += 5
udka = igrok('sd.png', 300, 0)

pts = 0

class vrag(sprait):

    
    def atack(self):

        self.ris()
        self.image = transform.scale(self.image, (40, 90))
        self.rect.y -= 5
        if self.rect.y <= -70:
            self.rect.y = 800
            self.rect.x = rd.randint(75, 525) 
    def collide(self, p):
            self.rect.y = 800
            self.rect.x = rd.randint(75, 525)
            global pts
            pts += 1
fish = vrag('fsh.png', rd.randint(75,525), 800)
fish2 = vrag('fsh.png', rd.randint(75,525), 800)



#f1 = font.Font(None, 36)
#text1 = f1.render(pts, True, (255,255,255))
#f1 = pygame.font.Font(None, 36)
#text1 = f1.render('press SPACE to start', True, (0,0,0))
game = True
yf1 = 0
yf2 = -700
yf3 = 700
hud = Surface((600, 50))

while game:
    okno.blit(fon1,(0,yf1))
    okno.blit(fon2,(0,yf2))
    okno.blit(fon3,(0,yf3))
    for i in event.get():
        if i.type == QUIT: 
            game = False
    udka.ris()
    udka.upravl()
    fish.atack()
    fish2.atack()
    if sprite.collide_rect(udka, fish):
        vrag.collide(fish, udka)
    if sprite.collide_rect(udka, fish2):
        vrag.collide(fish2, udka)
    yf1 -= 3
    yf2 -= 3
    yf3 -= 3
    if yf1 < -700:
        yf1 = 700
    if yf2 <-700:
        yf2 = 700
    if yf3 < -700:
        yf3 = 700
    okno.blit(hud, (0, 650))
    hud.fill((0,0,0))
    draw.rect(okno, (0,255,0), Rect(200,650,pts*8,30))
    draw.line(okno, (255,255,255), [300, 0], [udka.rect.x + 25, udka.rect.y + 5], 3)


    display.update()
