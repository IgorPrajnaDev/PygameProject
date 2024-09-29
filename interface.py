import pygame 
import sys
import cores


# iniciação do pygamge
pygame.init()

#resolução da tela
info = pygame.display.Info()
screen_width, screen_height = info.current_w, info.current_h
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)


#imagem de fundo
background_image = pygame.image.load(r'C:\Users\pedro\Desktop\Projeto Final IP\Imagens\pixel_wallpaper_by_simonesheri1_df0esjo-fullview.jpg')
background_image = pygame.transform.scale(background_image,(screen_width, screen_height))

#texto
font = pygame.font.SysFont("JetBrains-Mono", 30)

def draw_button(text, x, y, width, height, inactive_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    button_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    # Verifica se o mouse está sobre o botão
    if (x + width > mouse[0] > x and y + height > mouse[1] > y):
        # Desenhar um retângulo com a cor ativa
        pygame.draw.rect(screen, inactive_color + (0,), (x, y, width, height), 1, border_radius=50)  # Adicionando 100 para a transparência
        # Verifica se o botão foi clicado
        if click[0] == 1 and action is not None:
            action()
    else:
        # Desenhar um retângulo com a cor inativa
        button_surface.fill((128))  # Adicionando 100 para a transparência

    # Desenhar o texto do botão
    text_surf = font.render(text, True, (255, 255, 255))  # Cor do texto em branco
    text_rect = text_surf.get_rect(center=(x + width // 2, y + height // 2))
    screen.blit(text_surf, text_rect)

                                            
