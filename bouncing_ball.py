'''
Bouncing ball pygame demo.
Copied from http://www.pygame.org/docs/tut/PygameIntro.html
'''
import sys
import pygame
pygame.init()

# Width and height of the screen in pixels.
width = 640
height = 480
# List of speed. First item is the x speed, second is the y speed.
speed = [2, 2]
# RGB color for white
white = (255, 255, 255)
size = (width, height)
screen = pygame.display.set_mode(size)

# Load the ball.png image, which is stored in the same directory
# as this bouncing_ball.py file.
ball = pygame.image.load('ball.png')
# pygame.Rect object used in drawing
# https://www.pygame.org/docs/ref/rect.html#pygame.Rect
ballrect = ball.get_rect()

# Loop forever until the user quits the game.
while True:
    # Process all of the events the user input after the last frame
    # was drawn (e.g. mouse events and keyboard events).
    for event in pygame.event.get():
        # Quit the program when the user presses the x in the window.
        if event.type == pygame.QUIT:
            sys.exit()
        # Process events when the user presses key down.
        # https://www.pygame.org/docs/ref/key.html
        elif event.type == pygame.KEYDOWN:
            # Double the ball speed when the user presses the spacebar.
            if event.key == pygame.K_SPACE:
               speed[0] *= 2
               speed[1] *= 2
            # Halve the ball speed when the user presses enter.
            elif event.key == pygame.K_RETURN:
               speed[0] /= 2
               speed[1] /= 2

    # Move the rectangle the number of spaces according to the speed.
    ballrect = ballrect.move(speed)
    # Reverse the direction of the ball if it hits the edges.
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] *= -1
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] *= -1

    # Fill the screen with the white background. We draw the entire 
    # screen for each frame.
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.fill
    screen.fill(white)
    # Draw the ball on the screen.
    # https://www.pygame.org/docs/ref/surface.html#pygame.Surface.blit
    screen.blit(ball, ballrect)
    # Call flip after we're done drawing this frame. This updates the
    # entire display so the user can see the fill and blit operations
    # we just performed above.
    # https://www.pygame.org/docs/ref/display.html#pygame.display.flip
    pygame.display.flip()
