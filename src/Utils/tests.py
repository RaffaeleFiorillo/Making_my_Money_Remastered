import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
WHITE = (255, 255, 255)
R_OBJECTS_NUMBER = 1000

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Object Display Game")
clock = pygame.time.Clock()


class random_object:
	image = pygame.image.load(
		"C:/Users/Dark Knight/Desktop/Projects/Games/Making_my_Money_Remastered/assets/Images/Main Character/alive.png")
	image.convert_alpha()
	
	def __init__(self):
		self.x, self.y = random.randint(0, WIDTH), random.randint(0, HEIGHT)
	
	def draw(self, i_screen):
		i_screen.blit(self.image, (self.x, self.y))


# Load images for objects
objects = []  # [random_object() for i in range(R_OBJECTS_NUMBER)]
dts = []

# Main game loop
for i in range(10000):
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	# Clear the screen
	screen.fill(WHITE)

	# Display objects
	[o.draw(screen) for o in objects]

	# Update the display
	pygame.display.flip()

	# Cap the frame rate
	dt = clock.tick()/1000
	dts.append(1/dt+0.00000001)
	objects.append(random_object())
	
print(dts)
print(sum(dts)/len(dts))
