
class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def emitir_som(self):
        print("O animal emitiu um som genérico.")

class Cachorro(Animal):
    def emitir_som(self):
        print("O cachorro latiu!")

class Gato(Animal):
    def emitir_som(self):
        print("O gato miou!")

def main():
    meu_cachorro = Cachorro("Dodo", 5)
    meu_gato = Gato("Spaten", 3)

    meu_cachorro.emitir_som()  # Saída: O cachorro latiu!
    meu_gato.emitir_som()      # Saída: O gato miou!

main()