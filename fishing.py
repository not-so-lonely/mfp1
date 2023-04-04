from pygame import*


clock = time.Clock()#часы для игры
FPS = 120


okno = display.set_mode((600, 1000))

#fon0 = image.load('bg_sky.jpg')
fon1 = image.load("bg.jpg") 
fon2 = image.load("bg.jpg") 
fon3 = image.load("bg.jpg")
fon1 = transform.scale(fon1, (600, 1000)) 
fon2 = transform.scale(fon2, (600, 1000)) 
fon3 = transform.scale(fon3, (600, 1000)) 
#fon0 = transform.scale(fon0, (600, 200))


class sprait(sprite.Sprite):
    def __init__(self, kartinka, x, y):
        super().__init__()
        self.image = transform.scale(image.load(kartinka), (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def ris(self):
        okno.blit(self.image, (self.rect.x, self.rect.y))


class igrok(sprait):
    def upravl(self):
        self.ris()
        knopki = key.get_pressed()
        if knopki[K_RIGHT] and self.rect.x >= 50:
            self.rect.x -= 5
        if knopki[K_LEFT] and self.rect.X <= 550:
            self.rect.x += 5
udpchka = igrok('sd.png', 60, 80)









f1 = pygame.font.Font(None, 36)
text1 = f1.render('press SPACE to start', True, (0,0,0))


yf1 = 0
yf2 = -1000
yf3 = 1000
while game:
    okno.blit(fon1,(xf1,0))
    okno.blit(fon2,(xf2,0))
    okno.blit(fon3,(xf3,0))
        for i in event.get():
        if i.type == QUIT: 
            game = False
        if i.type == KEYDOWN:
            if i.key == K_SPACE:
                yf1 -= 3
                yf2 -= 3
                yf3 -= 3
