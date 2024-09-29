import pygame
import sys
import interface

def quit_game():
    pygame.quit()
    sys.exit()

def main():
    running = True
    pygame.mixer.init()
    pygame.mixer.music.load(r"C:\Users\pedro\Desktop\Projeto Final IP\Musicas\스텔라장(Stella Jang) - L’Amour, Les Baguettes, Paris_ Piano Cover _ Sheet.mp3")
    pygame.mixer.music.play(-1)
    #loop inicialização
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Desenhar a imagem de fundo
        interface.screen.blit(interface.background_image, (0, 0))

        # Desenhar botões
        interface.draw_button("Start", (interface.screen_width/2), 250, 150, 50, (66, 133, 244), action=None)  # Ação para ser definida
        interface.draw_button("Quit", (interface.screen_width/2), 750, 150, 50, (66, 133, 244), action=quit_game)

        # Atualizar a tela
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()