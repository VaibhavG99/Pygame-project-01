import pygame
import backplayer
from moviepy.editor import VideoFileClip

def play_intro():
    pygame.init()

    # Set up the window
    screen_width = 500
    screen_height = 700
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("MoviePy Video")

    # Load the video
    video = VideoFileClip('video1.avi')  # replace with the path to your video file

    # Main loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Get the current frame of the video
        frame = video.get_frame(pygame.time.get_ticks() / 1000)

        # Convert the frame to a Pygame surface
        surface = pygame.surfarray.make_surface(frame.swapaxes(0, 1))

        # Blit the surface onto the screen
        screen.blit(surface, (0, 0))

        # Update the display
        pygame.display.update()

        # Check if the video has ended
        if pygame.time.get_ticks() / 1000 >= video.duration:
            backplayer.bg_with_player()
            #pygame.quit()
            #quit()

            

