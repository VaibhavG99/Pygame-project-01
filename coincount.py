import pygame, sys
import random
from verticalplayer import player1

def coincount():

    pygame.init()

    #centre of images for collision

    def get_image_hcenter(image):
        """Get the center coordinates of an image in Pygame"""
        rect = image.get_rect()
        center_x = rect.centerx
        
        return center_x
    def get_image_vcenter(image):
        """Get the center coordinates of an image in Pygame"""
        rect = image.get_rect()
        center_y = rect.centery
        return center_y


    # Set up the window
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Falling Objects")

    # Set up the columns
    COLUMN_WIDTH = WINDOW_WIDTH // 4
    COLUMNS = [COLUMN_WIDTH * i for i in range(1,4)]


    #call for player from vertical player
    p = player1(250,WINDOW_HEIGHT-100)

        #movement of player
    moving_left = False
    moving_right = False

    # Load the object images
    object_images = []
    for i in range(1, 4):
        image = pygame.image.load(f"onecoin.jpg").convert_alpha()
        image2 = pygame.image.load(f"twocoins.jpg").convert_alpha()
        object_images.append(pygame.transform.scale(image, (120, 120)))
        object_images.append(pygame.transform.scale(image2, (120,120)))

    # Set up the clock
    clock = pygame.time.Clock()

    # Set up the variables for the falling object
    object_rect = None
    object_image = None
    falling = False
    falling_column = None
    collision=0
    score=0

    #text to be displayed
    font = pygame.font.SysFont('Arial', 30)

    # Set up the speed and the acceleration
    speed = 0.5
    acceleration = 0.0000001

    #collizion variables
    rect1 = pygame.Rect(get_image_hcenter(p.image),get_image_vcenter(p.image),100,20)
    rect2 = pygame.Rect(get_image_hcenter(image2),get_image_vcenter(image2),100,20)
    rect3 = pygame.Rect(get_image_hcenter(image),get_image_vcenter(image),100,20)


    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                sys.exit()

        # Check if an object is currently falling
        if not falling:
            # Randomly choose a column for the object to fall in
            falling_column = random.choice(COLUMNS)

            # Randomly choose an object image
            object_image = random.choice(object_images)

            # Set up the object's rect
            object_rect = object_image.get_rect(x=falling_column, y=0)

            # Set the falling flag to True
            falling = True

        # Move the object down the screen
        object_rect.y += speed
        speed += acceleration

        # Check if the object has reached the bottom of the screen
        if object_rect.y >= WINDOW_HEIGHT:
            # Reset the falling flag
            falling = False

        # Draw the columns
        for column in COLUMNS:
            pygame.draw.line(window, (255, 255, 255), (column, 0), (column, WINDOW_HEIGHT))

        # Draw the falling object
        if falling:
            window.blit(object_image, object_rect)
            #window.blit(object_image, object_rect)

        #movement control
        
            



            # Check for collision
        #if pygame.sprite.spritecollide(player1, image2, False):
            # game_over_text = font.render("Game Over", True, (0, 0, 0))
        # window.blit(game_over_text, (650, 200))
        # running = False


        if pygame.Rect.colliderect(rect1,rect3) == True:
            score= score+1
            

        if pygame.Rect.colliderect(rect1,rect2) == True:
            collision= collision +1
            running = False
            
        

        #update the score
        score_text = font.render("coins: " + str(score), True, (255, 0, 0))
        window.blit(score_text, (50, 20))



            # Update the display
        pygame.display.update()

        # Set the frame rate
        clock.tick(320)

        






    while running == False:

        # Game over screen
        game_over_text = font.render("Game Over", True, (255, 255, 255))
        window.blit(game_over_text, (250, 200))
        pygame.display.flip()

            




    # Quit the game
    pygame.quit()
