import tkinter as tk
from telas import TelaCadastro  # Importando a tela de cadastro
from animais import Cachorro, Gato  # Importando as classes de animais

def main():
    lista_animais = []  # Lista para armazenar os animais
    root = tk.Tk()
    tela_cadastro = TelaCadastro(root, lista_animais)
    root.mainloop()

if __name__ == "__main__":
    main()