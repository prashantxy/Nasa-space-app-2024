import pygame
import random

# Initialize pygame
pygame.init()

# Game window dimensions
WIDTH, HEIGHT = 1366, 768
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter")

# Set the clock
FPS = 60
clock = pygame.time.Clock()

# Colors
WHITE = (255, 255, 255)

# Load assets
PLAYER_IMG = pygame.image.load("C://Users//pdube//OneDrive//Desktop//NASA//main.js//test2//s1.png").convert_alpha()
ENEMY_IMG = pygame.image.load("C://Users//pdube//OneDrive//Desktop//NASA//main.js//test2//as1.png").convert_alpha()
BULLET_IMG = pygame.image.load("C://Users//pdube//OneDrive//Desktop//NASA//main.js//test2//b1.png").convert_alpha()
BG = pygame.image.load("C://Users//pdube//OneDrive//Desktop//NASA//main.js//test2//bg.png").convert_alpha()

# Resize images if necessary (optional)
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (150, 150))  # Adjust size as needed
ENEMY_IMG = pygame.transform.scale(ENEMY_IMG, (70, 70))  # Adjust size as needed
BULLET_IMG = pygame.transform.scale(BULLET_IMG, (10, 30))  # Adjust size as needed
BG = pygame.transform.scale(BG, (WIDTH, HEIGHT))

# Spaceship class
class Spaceship:
    def __init__(self):
        self.img = PLAYER_IMG
        self.x = WIDTH // 2
        self.y = HEIGHT - 100
        self.speed = 5
        self.bullets = []

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x - self.speed > 0:  # Move left
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x + self.speed + self.img.get_width() < WIDTH:  # Move right
            self.x += self.speed

    def shoot(self):
        # Position bullet slightly above the spaceship
        bullet = Bullet(self.x + self.img.get_width() // 2 - BULLET_IMG.get_width() // 2, self.y)
        self.bullets.append(bullet)

# Bullet class
class Bullet:
    def __init__(self, x, y):
        self.img = BULLET_IMG
        self.x = x
        self.y = y
        self.speed = -7

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y < 0

    def collision(self, obj):
        return collide(self, obj)

# Enemy class
class Enemy:
    def __init__(self, x, y):
        self.img = ENEMY_IMG
        self.x = x
        self.y = y
        self.speed = 2

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self):
        self.y += self.speed

    def off_screen(self):
        return self.y > HEIGHT

# Collision function
def collide(obj1, obj2):
    offset_x = obj2.x - obj1.x
    offset_y = obj2.y - obj1.y
    return obj1.img.get_rect().colliderect(obj2.img.get_rect().move(offset_x, offset_y))

# Main game function
def main():
    run = True
    spaceship = Spaceship()
    enemies = []
    score = 0
    lives = 5

    def redraw_window():
        WIN.blit(BG, (0, 0))  # Draw background
        spaceship.draw(WIN)   # Draw spaceship
        
        for enemy in enemies:
            enemy.draw(WIN)
        
        for bullet in spaceship.bullets:
            bullet.draw(WIN)

        # Display Score and Lives
        font = pygame.font.SysFont('comicsans', 30)
        score_text = font.render(f"Score: {score}", True, WHITE)
        lives_text = font.render(f"Lives: {lives}", True, WHITE)
        WIN.blit(score_text, (10, 10))
        WIN.blit(lives_text, (WIDTH - lives_text.get_width() - 10, 10))

        pygame.display.update()

    while run:
        clock.tick(FPS)
        redraw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Movement controls
        keys = pygame.key.get_pressed()
        spaceship.move(keys)

        # Shooting
        if keys[pygame.K_SPACE]:
            spaceship.shoot()

        # Move bullets
        for bullet in spaceship.bullets:
            bullet.move()
            if bullet.off_screen():
                spaceship.bullets.remove(bullet)

        # Generate enemies
        if random.randrange(0, 120) == 1:
            enemy = Enemy(random.randrange(50, WIDTH - 50), -100)
            enemies.append(enemy)

        # Move enemies
        for enemy in enemies:
            enemy.move()
            if enemy.off_screen():
                enemies.remove(enemy)
                lives -= 1  # Lose a life if an enemy passes the screen

        # Bullet-enemy collisions
        for bullet in spaceship.bullets:
            for enemy in enemies:
                if bullet.collision(enemy):
                    enemies.remove(enemy)
                    spaceship.bullets.remove(bullet)
                    score += 1

        if lives <= 0:
            font = pygame.font.SysFont('comicsans', 60)
            game_over_text = font.render("Game Over!", True, WHITE)
            WIN.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.delay(2000)  
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()
