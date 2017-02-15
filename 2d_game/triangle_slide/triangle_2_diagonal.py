import sys, pygame

BLACK = 0, 0, 0
WHITE = 255, 255, 255

pygame.init()
screen = pygame.display.set_mode((640,480))
pygame.display.set_caption("Diagonal Moving Triangle")

clock = pygame.time.Clock()

box_x = 300
box_y = 200
x_dir = 3
y_dir = 3

while 1:
  clock.tick(50)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

  screen.fill(BLACK)

  box_x += x_dir
  box_y += y_dir

  # Turn it around if goes all the way right
  if box_x >= 610:
    box_x = 610
    x_dir = -3
  # Turn it around it it gets all the way left
  elif box_x <= 0:
    box_x = 0
    x_dir = 3

  if box_y >= 480:
    box_y = 480
    y_dir = -3
  elif box_y <= 30:
    box_y = 30
    y_dir = 3

  pygame.draw.polygon(screen, WHITE, ((box_x, box_y), (box_x+30, box_y), (box_x+15,box_y-30)))
  pygame.display.flip()
