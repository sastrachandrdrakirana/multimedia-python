import pygame

# Inisialisasi pygame
pygame.init()

# Atur mode tampilan (misalnya, resolusi 800x600)
screen = pygame.display.set_mode((800, 600))

# Memuat gambar
image = pygame.image.load('jiro.jpg')

# Loop utama permainan dengan animasi
x = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Memperbarui posisi
    x += 5
    if x > 800:
        x = 0

    # Menggambar gambar di posisi baru
    screen.fill((0, 0, 0))  # Membersihkan layar dengan warna hitam
    screen.blit(image, (x, 100))

    # Memperbarui tampilan
    pygame.display.flip()

    # Menambahkan sedikit delay untuk kontrol frame rate (opsional)
    pygame.time.delay(30)

pygame.quit()
