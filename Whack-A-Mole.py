#Lennon Hudson

import pygame, random, sys, time
from pygame.locals import *



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (42, 140, 49)
RED = (255, 0, 0)
BLUE = (99, 147, 242)
YELLOW = (255,255,0)
LIGHTBLUE = (135, 206, 250)

def terminate():
   pygame.quit()
   sys.exit()


def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    terminate()
                return

def drawscreenbkgrd_moles(screen, x, y):
    screen.fill(GREEN)
    screen.blit(mole_Image,[10 + x, 20+ y])
    screen.blit(mole_Image, [200 + x, 20 + y])
    screen.blit(mole_Image, [390 + x, 20 + y])

def drawText(text, font, screen, x, y, clr):
    textobj = font.render(text, 1, clr)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    screen.blit(textobj, textrect)


pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Whack-A-Mole")



mole= pygame.Rect (10,10,100,143)
mole_Image = pygame.image.load("mole3.png")
player = pygame.Rect (10,10, 172, 238)
player_image = pygame.image.load("hammer2.png")
pygame.mixer.music.load("Thing_For_Itself_bkgrd.wav")
pygame.mixer.music.play(-1, 0.0)
hit_sound = pygame.mixer.Sound("hit_sfx.wav")
hit_zone = pygame.Rect(0 ,0, 35, 80)



mole_counter = 0
mole_remove = 0
NEWMOLES = 60
player_score = 0

font2 = pygame.font.SysFont(None, 48)




moles = []
for i in range(5):
    moles.append(pygame.Rect(random.randint(0, 600 - 20), random.randint(0, 367 - 20), 100, 143))
    print(len(moles))


#when player has x number of points draw more moles faster or make moles disappear faster(hammer up and down)
#redrawm moles
#fix print statemetns that aren't needed
#remove image not needed


#Screen 1 --Intro screen
drawscreenbkgrd_moles(screen,100,400)
drawText('Whack-A-Mole!', font2, screen, (700/3)-20, (500/3), BLACK)
drawText('Press any key to start.', font2, screen, (700/3)-50, (500/3)+ 130, BLACK)
pygame.display.update()
waitForPlayerToPressKey()


# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
timer = 6000


# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminate()
        if event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                terminate()
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for mole in moles:
                if mole.colliderect(hit_zone):
                    hit_sound.play()
                    moles.remove(mole)
                    player_score += 1
                    print("Player score: ", player_score)
    timer -= 1
    print(timer)
    # Screen 2 -- Ending screen
    if timer <= 0:
        drawscreenbkgrd_moles(screen, 100, 400)
        drawText("Your Score: " + str(player_score), font2, screen, (700 / 3) - 50, (500 / 3), BLACK)
        pygame.display.update()
        waitForPlayerToPressKey()

    # --- Game logic should go here

    mole_counter +=2
    if mole_counter >= NEWMOLES:
        mole_counter = 0
        moles.append(pygame.Rect(random.randint(0, 600 - 20), random.randint(0, 367 - 20), 100, 143))

    mole_remove += 1
    if mole_remove >= 120:
        mole_remove = 0
        moles.pop(0)
        player_score = player_score -2

    # If you want a background image, replace this clear with blit'ing the

    screen.fill(GREEN)

    #drawing score on screen
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render("Score:" + str(player_score), True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (65, 32)

    #drawing title on screen
    fontObj2 = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj2 = fontObj2.render("Whack-A-Mole!", True, BLACK)
    textRectObj2 = textSurfaceObj2.get_rect()
    textRectObj2.center = (350, 32)

    #drawing time on screen
    fontObj3 = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj3 = fontObj3.render("Time: " + str(timer), True, BLACK)
    textRectObj3 = textSurfaceObj3.get_rect()
    textRectObj3.center = (600, 32)

    #getting player position and hit zone
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    hit_zone.x = x
    hit_zone.y = y + 65

    pygame.mouse.set_visible(0)
    if x > 550:
        x = 600

    if y > 350:
        y = 350

    # bliting images to screen:
    for mole in moles:
        screen.blit(mole_Image, mole)

    screen.blit(player_image, [x, y])

    screen.blit(textSurfaceObj, textRectObj)
    screen.blit(textSurfaceObj2, textRectObj2)
    screen.blit(textSurfaceObj3, textRectObj3)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()