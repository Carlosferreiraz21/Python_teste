import tkinter as tk
from tkinter import ttk  # Importando ttk para usar o Notebook
from tkinter import messagebox
from animais import Cachorro, Gato

class TelaCadastro:
    def __init__(self, master, lista_animais):
        self.master = master
        self.lista_animais = lista_animais
        
        # Criando um Notebook (Abas)
        self.notebook = ttk.Notebook(self.master)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        # Criando as abas
        self.frame_cadastro = tk.Frame(self.notebook)
        self.frame_lista = tk.Frame(self.notebook)

        # Adicionando abas
        self.notebook.add(self.frame_cadastro, text="Cadastro")
        self.notebook.add(self.frame_lista, text="Lista de Animais")

        # Tela Cadastro
        self.criar_tela_cadastro()

        # Tela Lista de Animais
        self.criar_tela_lista()

    def criar_tela_cadastro(self):
        # Criando os widgets para a tela de cadastro
        self.label_nome = tk.Label(self.frame_cadastro, text="Nome:")
        self.label_nome.grid(row=0, column=0)
        self.entry_nome = tk.Entry(self.frame_cadastro)
        self.entry_nome.grid(row=0, column=1)

        self.label_idade = tk.Label(self.frame_cadastro, text="Idade:")
        self.label_idade.grid(row=1, column=0)
        self.entry_idade = tk.Entry(self.frame_cadastro)
        self.entry_idade.grid(row=1, column=1)

        self.label_animal = tk.Label(self.frame_cadastro, text="Tipo de Animal:")
        self.label_animal.grid(row=2, column=0)
        self.animal_combobox = ttk.Combobox(self.frame_cadastro, values=["Cachorro", "Gato"])
        self.animal_combobox.grid(row=2, column=1)

        self.label_porte_raca = tk.Label(self.frame_cadastro, text="Porte/Raça:")
        self.label_porte_raca.grid(row=3, column=0)
        self.entry_porte_raca = tk.Entry(self.frame_cadastro)
        self.entry_porte_raca.grid(row=3, column=1)

        self.btn_cadastrar = tk.Button(self.frame_cadastro, text="Cadastrar", command=self.cadastrar)
        self.btn_cadastrar.grid(row=4, columnspan=2)

    def cadastrar(self):
        nome = self.entry_nome.get()
        idade = self.entry_idade.get()
        tipo = self.animal_combobox.get()
        porte_raca = self.entry_porte_raca.get()

        if nome and idade.isdigit() and tipo and porte_raca:
            if tipo == "Cachorro":
                animal = Cachorro(nome, int(idade), porte_raca)
            elif tipo == "Gato":
                animal = Gato(nome, int(idade), porte_raca)
            self.lista_animais.append(animal)
            messagebox.showinfo("Cadastro", "Animal cadastrado com sucesso!")
            self.atualizar_lista()  # Atualiza a lista na aba "Lista de Animais"
        else:
            messagebox.showerror("Erro", "Preencha todos os campos corretamente!")

    def criar_tela_lista(self):
        self.lista_frame = tk.Frame(self.frame_lista)
        self.lista_frame.pack(padx=10, pady=10)

        # Criando um botão para atualizar a lista
        self.btn_atualizar = tk.Button(self.frame_lista, text="Atualizar Lista", command=self.atualizar_lista)
        self.btn_atualizar.pack(pady=10)

        # Label para mostrar os animais cadastrados
        self.lista_label = tk.Label(self.lista_frame, text="Animais Cadastrados:")
        self.lista_label.pack()

        self.lista_box = tk.Listbox(self.lista_frame, width=50, height=10)  # Caixa para exibir a lista
        self.lista_box.pack()

    def atualizar_lista(self):
        self.lista_box.delete(0, tk.END)  # Limpa a lista atual
        for animal in self.lista_animais:
            self.lista_box.insert(tk.END, f"{animal.getNome()} - {animal.getIdade()} anos")
