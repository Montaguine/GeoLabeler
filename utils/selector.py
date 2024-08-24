from matplotlib.widgets import RectangleSelector

class RectangleSelectorHandler:
    def __init__(self, ax, onselect):
        # Inicializa o RectangleSelector com os parâmetros fornecidos
        self.rect_selector = RectangleSelector(
            ax,  # O eixo onde o retângulo será desenhado
            onselect,  # Função de callback a ser chamada quando a seleção for concluída
            useblit=True,  # Usa blit para melhorar a performance
            button=[1],  # Botão do mouse usado para desenhar (1 = botão esquerdo)
            minspanx=5,  # Tamanho mínimo do retângulo na direção x
            minspany=5,  # Tamanho mínimo do retângulo na direção y
            spancoords='pixels',  # As coordenadas do retângulo são em pixels
            interactive=True  # Permite a interação com o retângulo após ser desenhado
        )

    def toggle_selector(self, event):
        # Ativa ou desativa o RectangleSelector com base na tecla pressionada
        if event.key in ['Q', 'q'] and self.rect_selector.active:
            print('Rectangle selector deactivated')
            self.rect_selector.set_active(False)
        if event.key in ['A', 'a'] and not self.rect_selector.active:
            print('Rectangle selector activated')
            self.rect_selector.set_active(True)