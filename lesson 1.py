import pygame
pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("test")

image1 = pygame.image.load("anime.jpg")
image_rect = image1.get_rect()

image2 = pygame.image.load("beer.png")
image_rect2 = image2.get_rect()
speed = 1

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = pygame.mouse.get_pos()
            image_rect.x = mouseX
            image_rect.y = mouseY
    if image_rect.colliderect(image_rect2):
        image_rect.x = 0
        image_rect.y = 0
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_UP:
#                 image_rect.y -= speed
#             elif event.key == pygame.K_DOWN:
#                 image_rect.y += speed
#             elif event.key == pygame.K_LEFT:
#                 image_rect.x -= speed
#             elif event.key == pygame.K_RIGHT:
#                 image_rect.x += speed



    screen.fill((6, 60, 90))
    screen.blit(image1, image_rect)
    screen.blit(image2, image_rect2)
    pygame.display.update()

pygame.quit()