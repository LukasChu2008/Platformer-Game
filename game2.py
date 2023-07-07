import pygame

pygame.init()

# # Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# # Set up the character
character_width = 50
character_height = 50
character_x = 0
character_y = screen_height - character_height
starting_position = 0, (0 - screen_height)
character_speed = 185  # pixels per second
character_jump_speed = 350  # pixels per second
character_gravity = 900  # pixels per second^2
character_velocity = [0, 0]

# # Set up the clock
clock = pygame.time.Clock()

# # Game loop
# while True:
#     # Handle events
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             pygame.quit()
#             quit()

#     # Get delta time
#     dt = clock.tick(60) / 1000.0  # 60 is the target frame rate

#     # Handle character movement
#     keys = pygame.key.get_pressed()
#     character_dx = 0
#     if keys[pygame.K_LEFT]:
#         character_dx = -character_speed * dt
#     elif keys[pygame.K_RIGHT]:
#         character_dx = character_speed * dt
#     character_x += character_dx

#     # Handle jumping
#     if keys[pygame.K_SPACE]:
#         character_velocity[1] = -character_jump_speed

#     # Handle gravity
#     character_dy = character_velocity[1] + character_gravity * dt
#     character_y += character_dy * dt
#     character_velocity[1] = character_dy

#     # Check for collisions with the ground and ceiling respectively
#     if character_y + character_height > screen_height:
#         character_y = screen_height - character_height
#         character_velocity[1] = 0
#     elif character_y <= 0:
#         character_y = 0
#         character_velocity[1] *= -1
    
#     # Check for collisions with the left and right wall respectively
#     if character_x <= 0:
#         character_x = 0
#     elif character_x + character_width >= screen_width:
#         character_x = screen_width - character_width

#     # Draw the character
#     screen.fill((255, 255, 255))
#     pygame.draw.rect(screen, (0, 0, 0), (character_x, character_y, character_width, character_height))
#     pygame.display.update()


import random

class Platform:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

# Set up the platforms
# Set up the platforms
platforms = []
platform_width = 100
platform_height = 20
num_sections = 5
section_height = screen_height / num_sections
for i in range(num_sections):
    x = random.randint(0, screen_width - platform_width)
    y = random.randint(int(i * section_height), int((i + 1) * section_height - platform_height))
    platforms.append(Platform(x, y, platform_width, platform_height))


# Game loop
while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    # Get delta time
    dt = clock.tick(60) / 1000.0  # 60 is the target frame rate

    # Handle character movement
    keys = pygame.key.get_pressed()
    character_dx = 0
    if keys[pygame.K_LEFT]:
        character_dx = -character_speed * dt
    elif keys[pygame.K_RIGHT]:
        character_dx = character_speed * dt
    character_x += character_dx

    # Handle jumping
    if keys[pygame.K_SPACE]:
        character_velocity[1] = -character_jump_speed

    # Handle gravity
    character_dy = character_velocity[1] + character_gravity * dt
    character_y += character_dy * dt
    character_velocity[1] = character_dy

    # Check for collisions with platforms
    for platform in platforms:
        if platform.rect.colliderect(character_x, character_y, character_width, character_height):
            if character_velocity[1] < 0:  # Character is moving upwards
                character_y = platform.rect.bottom
                character_velocity[1] = 0
            else:
                character_y = platform.rect.top - character_height
                character_velocity[1] = 0


    # Check for collisions with the ground and ceiling respectively
    if character_y + character_height > screen_height:
        character_y = screen_height - character_height
        character_velocity[1] = 0
    elif character_y <= 0:
        character_y = 0
        character_velocity[1] *= -1
    
    # Check for collisions with the left and right wall respectively
    if character_x <= 0:
        character_x = 0
    elif character_x + character_width >= screen_width:
        character_x = screen_width - character_width

    # Draw the platforms and the character
    screen.fill((255, 255, 255))
    for platform in platforms:
        pygame.draw.rect(screen, (0, 0, 255), platform.rect)
    pygame.draw.rect(screen, (0, 0, 0), (character_x, character_y, character_width, character_height))
    pygame.display.update()
