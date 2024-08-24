import tkinter as tk
from tkinter import scrolledtext

class Logger:
    def __init__(self, parent):
        # Cria um widget de texto com rolagem dentro do widget pai fornecido
        self.log_text = scrolledtext.ScrolledText(parent, wrap=tk.WORD, width=40, height=30)
        # Posiciona o widget de texto na grade do layout
        self.log_text.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    def log_message(self, message):
        # Insere a mensagem no final do widget de texto
        self.log_text.insert(tk.END, message + '\n')
        # Faz o widget de texto rolar até o final para mostrar a nova mensagem
        self.log_text.see(tk.END)
        # Imprime a mensagem no console
        print(message)