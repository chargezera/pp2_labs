import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 805))
done = False

mback = pygame.image.load('images/mback.jpg')
m1 = pygame.image.load('images/m1.jpg')
m1 = pygame.transform.scale(m1, (300, 300))
m2 = pygame.image.load('images/m2.webp')
m2 = pygame.transform.scale(m2, (300, 300))
m3 = pygame.image.load('images/m3.jpeg')
m3 = pygame.transform.scale(m3, (300, 300))
stop = pygame.image.load('images/stop.png')
stop = pygame.transform.scale(stop, (400, 400))
songs = ['sounds/s1.mp3', 'sounds/s2.mp3', 'sounds/s3.mp3']


clock = pygame.time.Clock()
playing = 1
prevPlay = 0
pygame.mixer.music.load(songs[0])
pygame.mixer.music.play()
played = True

while not done:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True
                if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RIGHT:
                            if(playing != 0):
                                if playing<3:
                                    playing+=1
                                else:
                                    playing=1
                        elif event.key == pygame.K_LEFT:
                            if(playing != 0):
                                if playing>1:
                                    playing-=1
                                else:
                                    playing=3
                        elif event.key == pygame.K_DOWN:
                              prevPlay = playing
                              playing = 0
                        elif event.key == pygame.K_UP:
                              if(playing == 0):
                                playing = prevPlay
                        played = False

                screen.blit(mback, (0,0))

                if(playing==1):
                        screen.blit(m1, (500, 225))
                        if(not played):
                            pygame.mixer.music.load(songs[0])
                            pygame.mixer.music.play()
                            played = True
                elif(playing==2):
                        screen.blit(m2, (500, 225))
                        if(not played):
                            pygame.mixer.music.load(songs[1])   
                            pygame.mixer.music.play()
                            played = True
                elif(playing==3):
                        screen.blit(m3, (500, 225))
                        if(not played):
                              pygame.mixer.music.load(songs[2])
                              pygame.mixer.music.play()
                              played = True
                elif(playing==0):
                        pygame.mixer.music.stop()
                        screen.blit(stop, (450, 200))

                pygame.display.flip()
                clock.tick(10)
