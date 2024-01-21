import pygame
import sys
from src.Utils.GAME_conf import SCREEN, BACKGROUND_IMAGE
from src.GameEntities import Agents
from src.GameEntities.Collectables import CollectableManager


class Base_Game:
	BACKGROUND_MUSIC = pygame.mixer.Sound("assets/Sounds/background music.mp3")
	GAME_OVER_SOUND = pygame.mixer.Sound("assets/Sounds/game over.mp3")
	FONT = pygame.font.SysFont("killer", 60)
	GAME_OVER_TEXT = FONT.render("You Died!!!", 1, (255, 0, 0))

	def __init__(self):
		self.game_over_message = "The game reached an End"
		
		self.background_image = BACKGROUND_IMAGE
		self.screen = SCREEN
		
		self.main_character = Agents.Me()
		self.enemy_manager = Agents.EnemyManager()
		self.collectable_manager = CollectableManager()
		
		self.key_is_pressed_in_x = False
		self.key_is_pressed_in_y = False
		
		self.clock = pygame.time.Clock()
		self.dt = 0  # delta time: time between frames expressed in milliseconds
		self.is_running = True
	
	def start(self):
		self.game_loop()
	
	# ------------------------ Managements --------------------------------
	def player_input_management(self, event):
		# Check if the player presses or releases a button
		if event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
			pressed_keys = pygame.key.get_pressed()
			# Update the speed based on the currently pressed keys
			self.main_character.change_speed_y(pressed_keys[pygame.K_DOWN] - pressed_keys[pygame.K_UP])
			self.main_character.change_speed_x(pressed_keys[pygame.K_RIGHT] - pressed_keys[pygame.K_LEFT])
		
	def manage_input(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()
			
			self.player_input_management(event)
	
	def manage_collisions(self):
		# enemy collisions
		for enemy in self.enemy_manager.enemies:
			self.main_character.is_colliding_with_enemy(enemy.hitbox)
		
		# life and money collisions
		for collectable in self.collectable_manager.collectables:
			self.main_character.is_colliding_with_collectable(collectable)
	
	# ------------------------ Game Loop --------------------------------------
	def update(self):
		self.main_character.update(self.dt)
		self.enemy_manager.update(self.dt)
		self.collectable_manager.update(self.dt)
	
	def draw(self):
		self.screen.blit(self.background_image, (0, 0))
		self.main_character.draw(self.screen)
		self.enemy_manager.draw_enemies(self.screen)
		self.collectable_manager.draw_collectables(self.screen)
		pygame.display.update()
	
	def game_loop(self):
		self.BACKGROUND_MUSIC.play(1)
		while self.main_character.is_alive():
			self.manage_input()
			self.manage_collisions()
			
			self.update()
			self.draw()
			self.dt = self.clock.tick(60) / 1000  # updating delta time
		
		self.game_over()
	
	def game_over(self):
		self.GAME_OVER_SOUND.play()
		self.screen.fill((0, 0, 0))
		self.screen.blit(self.GAME_OVER_TEXT, (390, 300))
		pygame.display.update()
		
		for i in range(200):
			self.clock.tick(30)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
		
		pygame.quit()
		sys.exit()
