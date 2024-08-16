# Memuat gambar
import pygame

# Inisialisasi pygame
pygame.init()

# Atur mode tampilan (misalnya, resolusi 800x600)
screen = pygame.display.set_mode((800, 600))

# Memuat gambar
image = pygame.image.load('jiro.jpg')

# Loop utama permainan
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Menggambar gambar di posisi (100, 100)
    screen.blit(image, (100, 100))

    # Memperbarui tampilan
    pygame.display.flip()

# Keluar dari pygame
pygame.quit()
