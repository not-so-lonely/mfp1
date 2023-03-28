from pygame import*


clock = time.Clock()#часы для игры
FPS = 120


okno = display.set_mode((600, 1000))



fon1 = image.load("bg.jpg") 
fon2 = image.load("bg.jpg") 
fon3 = image.load("bg.jpg")
fon1 = transform.scale(fon1, (600, 1000)) 
fon2 = transform.scale(fon2, (600, 1000)) 
fon3 = transform.scale(fon3, (600, 1000)) 
