import sys, pygame
BACKGROUND = (255,255,255)
SHAPE_COLOR = (95,72,138)
SHAPE_COLOR1 = (24,18,75)
pygame.init()

screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("My pygame!")

clock = pygame.time.Clock()
box_x = 300
box_dir = 3

while True:
    clock.tick(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(BACKGROUND)

    box_x = box_x + box_dir
    if box_x >= 620:
        box_dir = -3
    elif box_x <= 0:
        box_dir = 3

    pygame.draw.polygon (screen, SHAPE_COLOR, ((box_x, box_x/2),(box_x/5+500,200), (200,300)))
    pygame.draw.polygon (screen, SHAPE_COLOR1, ((box_x, 200),(200,200), (200,300)))

    pygame.display.flip()
