from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def mostrar(self):
        print(f"Nome: {self.nome}, Idade: {self.idade}")
    
    def getNome(self):
        return self.nome
    
    def getIdade(self):
        return self.idade
    
    def setNome(self, nome):
        self.nome = nome
    
    def setIdade(self, idade):
        self.idade = idade

class Cachorro(Animal):
    def __init__(self, nome, idade, porte):
        super().__init__(nome, idade)
        self.porte = porte
    
    def setPorte(self, porte):
        self.porte = porte
    
    def getPorte(self):
        return self.porte
    
    def mostrar(self):
        super().mostrar()
        print(f"Porte: {self.porte}")

class Gato(Animal):
    def __init__(self, nome, idade, raca):
        super().__init__(nome, idade)
        self.raca = raca
    
    def setRaca(self, raca):
        self.raca = raca
    
    def getRaca(self):
        return self.raca
    
    def mostrar(self):
        super().mostrar()
        print(f"Raça: {self.raca}")
