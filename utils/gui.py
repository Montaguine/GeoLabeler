import tkinter as tk
from tkinter import filedialog
from PIL import Image
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from utils.logger import Logger
from utils.selector import RectangleSelectorHandler
from utils.config import categories, initial_category, initial_subcategory
import numpy as np

class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.annotations = []
        self.current_label = initial_subcategory
        self.rect_selector = None

        self.setup_gui()

    def setup_gui(self):
        # Solicita ao usuário que selecione um arquivo de imagem
        image_path = filedialog.askopenfilename(title="Select an image file", filetypes=[("Image files", "*.tif;*.jpg;*.png")])
        if not image_path:
            print("No image file selected. Exiting.")
            return

        # Solicita ao usuário que selecione um local para salvar
        self.save_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if not self.save_path:
            print("No save location selected. Exiting.")
            return

        # Carrega a imagem
        img = Image.open(image_path)
        fig, ax = plt.subplots()
        ax.imshow(img)
        plt.axis('off')

        # Inicializa o RectangleSelector
        self.rect_selector_handler = RectangleSelectorHandler(ax, self.onselect)

        # Cria um frame para o menu
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(side=tk.LEFT, fill=tk.Y, expand=False)

        # Cria e exibe o dropdown de seleção de categoria com rótulo
        category_label = tk.Label(menu_frame, text="Classe")
        category_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')
        category_var = tk.StringVar(self.root)
        category_var.set(initial_category)
        category_selector = tk.OptionMenu(menu_frame, category_var, *categories.keys(), command=self.update_subcategories)
        category_selector.grid(row=0, column=1, padx=5, pady=5, sticky='w')

        # Cria e exibe o dropdown de seleção de subcategoria com rótulo
        subcategory_label = tk.Label(menu_frame, text="Subclasse")
        subcategory_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')
        self.subcategory_var = tk.StringVar(self.root)
        self.subcategory_var.set(initial_subcategory)
        self.subcategory_selector = tk.OptionMenu(menu_frame, self.subcategory_var, *categories[initial_category], command=self.update_label)
        self.subcategory_selector.grid(row=1, column=1, padx=5, pady=5, sticky='w')

        # Adiciona um widget de texto com rolagem para o log
        self.logger = Logger(menu_frame)

        # Adiciona um botão de salvar
        save_button = tk.Button(menu_frame, text="Salvar e sair", command=self.save_and_exit)
        save_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky='s')

        # Incorpora a figura do Matplotlib na janela Tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.root)
        canvas.draw()
        canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.root.deiconify()

        # Centraliza a janela e define seu tamanho para 70% da tela
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        window_width = int(screen_width * 0.7)
        window_height = int(screen_height * 0.7)
        position_x = screen_width // 2 - window_width // 2
        position_y = screen_height // 2 - window_height // 2
        self.root.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

        # Conecta a função toggle_selector aos eventos de pressionamento de tecla
        fig.canvas.mpl_connect('key_press_event', self.rect_selector_handler.toggle_selector)

        # Trata o evento de fechamento da janela
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def update_subcategories(self, selected_category):
        subcategories = categories[selected_category]
        self.subcategory_var.set(subcategories[0])
        menu = self.subcategory_selector["menu"]
        menu.delete(0, "end")
        for subcategory in subcategories:
            menu.add_command(label=subcategory, command=lambda value=subcategory: self.update_label(value))
        self.update_label(self.subcategory_var.get())

    def update_label(self, selected_subcategory):
        self.current_label = selected_subcategory
        self.subcategory_var.set(selected_subcategory)  # Atualiza o texto do botão do OptionMenu

    def onselect(self, eclick, erelease):
        if self.current_label is None:
            self.logger.log_message("No class selected. Please select a class from the dropdown.")
            return
        rect = [
            np.float64(eclick.xdata), np.float64(eclick.ydata), np.float64(erelease.xdata), np.float64(erelease.ydata),
            self.current_label
        ]
        self.annotations.append(rect)
        self.logger.log_message("Quadrante adicionado:")
        self.logger.log_message(f"X1: {eclick.xdata}")
        self.logger.log_message(f"Y1: {eclick.ydata}")
        self.logger.log_message(f"X2: {erelease.xdata}")
        self.logger.log_message(f"Y2: {erelease.ydata}")
        self.logger.log_message(f"Classe: {self.current_label}")
        self.logger.log_message(f"")

        # self.logger.log_message("Anotações atuais:")
        # for annotation in self.annotations:
        #     x1, y1, x2, y2, label = annotation
        #     self.logger.log_message(f"X1: {x1}, Y1: {y1}, X2: {x2}, Y2: {y2}, Classe: {label}")

    def save_and_exit(self):
        self.save_annotations(self.save_path)
        self.on_closing()

    def save_annotations(self, save_path):
        import csv
        with open(save_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["X1", "Y1", "X2", "Y2", "Label"])
            for annotation in self.annotations:
                writer.writerow(annotation)
        self.logger.log_message(f"Annotations saved to {save_path}")

    def on_closing(self):
        self.root.quit()
        self.root.destroy()

    def run(self):
        self.root.mainloop()