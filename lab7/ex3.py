import pygame

pygame.init()
screen = pygame.display.set_mode((800, 800))
done = False
is_blue = True
x = 400
y = 400

clock = pygame.time.Clock()

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
        
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]: 
            if y-20 > 0:
                y -= 20
        if pressed[pygame.K_DOWN]: 
            if y+20 < 800:  
                y += 20
        if pressed[pygame.K_LEFT]: 
            if x-20 > 0:
                x -= 20
        if pressed[pygame.K_RIGHT]:
            if x+20 < 800:
                x += 20

        
        screen.fill((255, 255, 255))
        color = (255, 0, 0)
        circle = pygame.draw.circle(screen, color, (x, y), 25)
        
        pygame.display.flip()
        clock.tick(60)