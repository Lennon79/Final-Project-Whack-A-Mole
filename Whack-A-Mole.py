#Lennon Hudson
import pygame,random,sys,time
from pygame.locals import *


# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (42, 140, 49)
RED = (255, 0, 0)
BLUE = (99, 147, 242)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Whack-A-Mole")

start_ticks = pygame.time.get_ticks()
seconds = (pygame.time.get_ticks() - start_ticks) / 1000

mole= pygame.Rect (10,10,100,143)
mole_Image = pygame.image.load("mole3.png")
player = pygame.Rect (10,10, 172, 238)
player_image = pygame.image.load("hammer2.png")
#pygame.mixer.music.play(-1,0.0)
#click_sound = pygame.mixer.Sound(" ")

hit_zone = pygame.Rect(0 ,0, 35, 80)

moles = []
mole_number = 0
for i in range(5):
    moles.append(pygame.Rect(random.randint(0, 600 - 20), random.randint(0, 367 - 20), 100, 143))
    mole_number += 1
    print(mole_number)


moleCounter = 0
NEWMOLES = 60
NEWMOLES2 = 30
player_score = 0
def terminate():
   pygame.quit()
   sys.exit()




#redraw moles, pick bkgrd music and hit sfx(hammer sound, mole reaction sound[in collison])
#add op screen
#timer on screen
#when player has x number of points draw more moles faster
#moles and game on timer
#take away points when mole is missed
#make sure moles don't draw on eachother




# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

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
                    # click_sound.play() make a noise when mole is hit
                    moles.remove(mole)
                    mole_number = mole_number - 1
                    player_score += 1
                    print(mole_number)
                    print("Player score: ", player_score)  # calculate how many seconds
        if seconds > 10:  # if more than 10 seconds close the game
            terminate()
            print(seconds)
        #https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect


    # --- Game logic should go here
    moleCounter +=1
    if moleCounter >= NEWMOLES:
        moleCounter = 0
        moles.append(pygame.Rect(random.randint(0, 600 - 20), random.randint(0, 367 - 20), 100, 143))
        mole_number += 1
        print(mole_number)



    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here

    #drawing score on screen
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render("Score:" + str(player_score), True, BLACK)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (65, 32)

    #drawing time on screen

    #getting player position and hit zone
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    hit_zone.x = x
    hit_zone.y = y + 65

    pygame.mouse.set_visible(0)
    if x > 550:
        x = 550

    if y > 350:
        y = 350

    # bliting images to screen:
    for mole in moles:
        screen.blit(mole_Image, mole)

    screen.blit(player_image, [x, y])

    screen.blit(textSurfaceObj, textRectObj)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()