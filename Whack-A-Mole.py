#Lennon Hudson
import pygame,random,sys

#import sys

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

'''def draw_holes(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [x, y, 150, 50], )
    pygame.draw.ellipse(screen, BLACK, [x+200, y, 150, 50], )
    pygame.draw.ellipse(screen, BLACK, [x+400, y, 150, 50], )
    pygame.draw.ellipse(screen, BLACK, [x+100, y+150, 150, 50], )
    pygame.draw.ellipse(screen, BLACK, [x+300, y+150, 150, 50], )
    [80, 260], [280, 260], [480, 260],[180,310],[380, 310]'''



mole= pygame.Rect (3,3,100,143)
mole_Image = pygame.image.load("mole3.png")
moleStretchedImage = pygame.transform.scale(mole_Image, (1,1))
player = pygame.Rect (10,10, 5, 15)
player_image = pygame.image.load("hammer2.png")
playerStretchedImage = pygame.transform.scale(player_image, (5, 5))
#pygame.mixer.music.play(-1,0.0)
#hit_sound = pygame.mixer.Sound(" ")



moles = []
for i in range(5):
    moles.append(pygame.Rect(random.randint(0, 600 - 20), random.randint(0, 367 - 20), 100, 143))
    #mole = random.randrange(len(moles))
    #print(mole)



#mole collison with hammer(when moles are clicked they disappear)
#add music and sfx
#moles and game on timer
#add points when mole is hit
#add op screen





# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            sys.exit()
        #if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            #if mole.collidepoint(player_position):
                #click_sound.play() make a noise when mole is hit
        #https://stackoverflow.com/questions/12150957/pygame-action-when-mouse-click-on-rect


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(GREEN)

    # --- Drawing code should go here


    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    pygame.mouse.set_visible(0)
    if x > 550:
        x = 550

    if y > 350:
        y = 350

    # Copy image to screen:
    for mole in moles:
        screen.blit(mole_Image, mole)

    screen.blit(player_image, [x, y])

    #screen.blit(mole_Image,[mole])#blit moles
    for mole in moles[:]:
       if mole.collidepoint(player_position):
           moles.remove(mole)



    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()