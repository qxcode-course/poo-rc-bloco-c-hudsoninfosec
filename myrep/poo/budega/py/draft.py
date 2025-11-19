class Person:
    def __init__(self,nome: str):
        self.__nome = nome

    def getNome(self):
        return self.__nome
    
    def __str__(self):
        return f'{self.__nome}'
    
class Market:
    def __init__(self, n_caixas: int):
        self.espera: list[Person] = []
        self.caixas: list[Person | None] = []
        
        for i in range(n_caixas):
            self.caixas.append(None)
    
    def __str__(self):
        caixas = ', '.join([str(x)if x else '-----' for x in self.caixas])
        espera = ', '.join([str(x) for x in self.espera])

        return f'Caixas: [{caixas}]\nEspera: [{espera}]'
    
    def arrive(self, cliente : Person):
        self.espera.append(cliente)

    def call(self, index: int):
        if index < 0 or index >= len(self.caixas):
            print('index invalido')
            return
        if self.caixas[index] is not None:
            print('fail: caixa ocupado')
            return
        if len(self.espera) == 0:
            print('fail: sem clientes')
            return
        
        self.caixas[index] = self.espera.pop(0)
    
    def finish(self, index: int) -> Person | None:
        if index < 0 or index >= len(self.caixas):
            print('fail: caixa inexistente')
            return None
        if self.caixas[index] is None:
            print('fail: caixa vazio')
            return None
        
        aux = self.caixas[index]
        self.caixas[index] = None
        return aux
    
def main():
        mercado = None

        while True:
            line = input()
            print("$" + line)
            args : list[str] = line.split()

            if args[0] == 'end':
                break
            elif args[0] == 'show':
                print(mercado)
            elif args[0] == 'init':
                qtd = int(args[1])
                mercado = Market(qtd)
            elif args[0] == 'arrive':
                nome = args[1]
                mercado.arrive(Person(nome))
            elif args[0] == 'call':
                index = int(args[1])
                mercado.call(index)
            elif args[0] == 'finish':
                index = int(args[1])
                mercado.finish(index)

main()