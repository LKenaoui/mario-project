# mario-project

# Initialiser Pygame
pygame.init()

# Créer une fenêtre
window = pygame.display.set_mode(window_size)

# Régler la taille de la fenêtre
window_size = (640, 480)

# Créer un Sprite de personnage
player = Player(320, 240, 0, 0)
    
# Mettre à jour le Sprite du personnage
player.update()

# Effacer la fenêtre
window.fill((255, 255, 255))

# Dessiner le Sprite du personnage
player.draw(window)

# Mettre à jour l'affichage
pygame.display.update()