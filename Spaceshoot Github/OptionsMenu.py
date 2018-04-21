import pygame
import os

pygame.init()
game_width = 480
game_height = 600
fps = 60

pygame.mixer.init()
screen = pygame.display.set_mode((game_width, game_height))
pygame.display.set_caption("Shoot!")
clock = pygame.time.Clock()

white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)

game_path = os.path.dirname(__file__)
img_path = os.path.join(game_path, "images")

font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, white)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

def OptionsMenu():
    screen.blit(background, background_rect)
    draw_text(screen, "Options Menu", 25, game_width/2, 40)
    draw_text(screen, "Choose Player", 22, game_width/2, game_height/6)


#loading images

bullet_img = pygame.image.load(os.path.join(img_path, "laserGreen03.png")).convert()


bullet_img = pygame.image.load(os.path.join(img_path, "laserRed13.png")).convert()


bullet_img = pygame.image.load(os.path.join(img_path, "laserBlue12.png")).convert()
Mouse = pygame.mouse.get_pos()