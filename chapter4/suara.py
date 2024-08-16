import pygame  # Pastikan pygame diimpor

# Inisialisasi pygame
pygame.init()

# Inisialisasi mixer untuk memutar suara
pygame.mixer.init()

# Memuat suara
sound = pygame.mixer.Sound('track.wav')

# Memutar suara
sound.play()

# Loop utama permainan agar suara terus diputar hingga selesai
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Keluar dari pygame
pygame.quit()
