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

def draw_holes(screen, x, y):
    pygame.draw.ellipse(screen, BLACK, [x, y, 150, 50], )
    pygame.draw.ellipse(screen, BLACK, [x+200, y, 150, 50], )
    pygame.draw.ellipse(screen, BLACK, [x+400, y, 150, 50], )
    pygame.draw.ellipse(screen, BLACK, [x+100, y+150, 150, 50], )
    pygame.draw.ellipse(screen, BLACK, [x+300, y+150, 150, 50], )


player = pygame.Rect (10,10, 5, 15)
player_image = pygame.image.load("hammer2.png")
playerStretchedImage = pygame.transform.scale(player_image, (5, 5))
mole_rect = pygame.Rect (3,3,2,1)
mole_Image = pygame.image.load("mole3.png")
moleStretchedImage = pygame.transform.scale(mole_Image, (1,1))

moles = [[80, 260], [280, 260], [480, 260],[180,310],[380, 310]]
for i in range(5):

    #blit mole_Image at random coordinate in moles list
    mole = random.randrange(len(moles))
    print(mole)




#pygame.mixer.music.play(-1,0.0)
#click_sound = pygame.mixer.Sound("laser5.ogg")

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
            #elif event.type == pygame.MOUSEBUTTONDOWN:
                #click_sound.play() make a noise when mole is hit


    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)

    # --- Drawing code should go here
    pygame.draw.rect(screen, GREEN, [0, 250, 700, 250], 0)
    draw_holes(screen, 80, 260)

    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
    pygame.mouse.set_visible(0)
    if x > 550:
        x = 550

    if y > 350:
        y = 350

    # Copy image to screen:
    screen.blit(player_image, [x, y])
    screen.blit(mole_Image,[100,210])#blit moles


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()