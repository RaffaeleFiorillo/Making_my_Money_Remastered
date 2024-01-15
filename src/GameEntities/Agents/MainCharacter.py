import pygame
from src.GameEntities.Agents.BaseAgent import Base
from src.GameEntities.Collectables import Collectable


class Me(Base):
    IMAGE = pygame.image.load("assets/Images/Main Character/alive.png").convert_alpha()
    DEATH_IMAGE = pygame.image.load("assets/Images/Main Character/dead.png").convert_alpha()
    DEATH_SOUND = pygame.mixer.Sound("assets/Sounds/main character death.mp3")
    COOL_DOWN_TIME = 2  # immunity time after an enemy hits you
    FONT = pygame.font.SysFont("comicsans", 30, True)
    
    def __init__(self, x=465, y=300):
        super().__init__(x, y)
        self.image = self.IMAGE
        self.size = tuple(self.image.get_size())
        
        self.money = 0  # serves as the game's score
        self.lives = 5  # number of lives. When it reaches 0 it is Game Over
        self.cool_down_timer = 0  # if the timer is higher than 0, the Main Character has immunity
        
        self.has_immunity = lambda: self.cool_down_timer > 0
        self.is_alive = lambda: self.lives > 0

    # ---------------------------- Collisions Effects ------------------------------------
    def _apply_money_collision_effect(self, money: Collectable):
        money.apply_collected_effect()
        self.money += money.value

    def _apply_cure_collision_effect(self, cure: Collectable):
        cure.apply_collected_effect()
        self.lives += cure.value
    
    def _apply_enemy_collision_effect(self):
        self.DEATH_SOUND.play()
        self.image = self.DEATH_IMAGE
        self.lives -= 1
        self.x = 465
        self.y = 300
        self.cool_down_timer = self.COOL_DOWN_TIME
        
    # -------------------------- Collisions Detection -----------------------------------
    def _is_colliding_with_hitbox(self, hitbox):
        # Check for collision along the x-axis
        if self.hitbox[0] < hitbox[0] + hitbox[2] and self.hitbox[0] + self.hitbox[2] > hitbox[0]:
            # Check for collision along the y-axis
            if self.hitbox[1] < hitbox[1] + hitbox[3] and self.hitbox[1] + self.hitbox[3] > hitbox[1]:
                return True
        return False

    def is_colliding_with_collectable(self, collectable: Collectable):
        if self._is_colliding_with_hitbox(collectable.hitbox):
            if collectable.type == "Money":
                self._apply_money_collision_effect(collectable)
            else:
                self._apply_cure_collision_effect(collectable)
            
    def is_colliding_with_enemy(self, enemy_hitbox: (int, int, int, int)):
        if not self.has_immunity() and self._is_colliding_with_hitbox(enemy_hitbox):
            self._apply_enemy_collision_effect()
  
    # ------------------------------ General --------------------------------------------
    def update(self, dt):
        super().update(dt)
        self.cool_down_timer = min(self.COOL_DOWN_TIME, max(0, self.cool_down_timer - 1*dt))
        
    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.FONT.render(str(self.money), True, (0, 255, 255)), (140, 5))
        [pygame.draw.rect(screen, (0, 255, 0), (542+25*i, 25, 20, 6)) for i in range(self.lives)]
