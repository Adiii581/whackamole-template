import pygame
import random
def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        screen_width = 640
        screen_height = 512
        gridSquare_size = 32
        gridLine_color = (0, 0, 0)
        mole_x_position = 0
        mole_y_position = 0
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x_position, mouse_y_position = event.pos
                    mole_image_on_grid = mole_image.get_rect(topleft=(mole_x_position * gridSquare_size, mole_y_position * gridSquare_size))
                    if mole_image_on_grid.collidepoint(mouse_x_position, mouse_y_position):
                        mole_x_position = random.randrange(0, (screen_width//gridSquare_size))
                        mole_y_position = random.randrange(0, (screen_height//gridSquare_size))
            screen.fill("light green")
            color = (0, 0, 0)
            for x in range(0, screen_width, gridSquare_size):
                pygame.draw.line(screen, gridLine_color, (x, 0), (x, screen_height))
            for y in range(0, screen_height, gridSquare_size):
                pygame.draw.line(screen, gridLine_color, (0, y), (screen_width, y))
            mole_image_on_grid = mole_image.get_rect(topleft=(mole_x_position * gridSquare_size, mole_y_position * gridSquare_size))
            screen.blit(mole_image, mole_image_on_grid)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
