class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int ):
        self.calibre = calibre 
        self.dureza = dureza 
        self.tamanho = tamanho

    def gastarFolha(self) -> int:
        if self.dureza == "HB":
            return 1
        elif self.dureza == "2B":
            return 2 
        elif self.dureza == "4B":
            return 4 
        elif self.dureza == "6B":
            return 6
        else:
            return 0 
        
    def __str__(self) -> str:
        return f"[{self.calibre}:{self.dureza}:{self.tamanho}]"

class Lapiseira:
    def __init__(self, calibre: float):
        self.calibre = calibre
        self.bico: Grafite | None = None 
        self.tambor: list[Grafite] = []

    def __str__(self ) :
        bico = str(self.bico) if self.bico else "[]"
        tambor = "".join(str(g) for g in self.tambor)
        tambor = f"<{tambor}>"
        return f"calibre: {self.calibre}, bico: {bico}, tambor: {tambor}"
    
    def inserir(self, grafite: Grafite) -> bool:
        if grafite.calibre != self.calibre:
            return False
        
        self.tambor.append(grafite)
        return True
    def puxar(self):
        if self.bico is not None:
            print("fail: ja existe grafite no bico")
            return 
        if not self.tambor:
            print("fail: tambor vazio ")
            return 
        self.bico = self.tambor.pop(0)

    def remover(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        self.bico = None
    
    def escrever(self):
        if self.bico is None:
            print("fail: nao existe grafite no bico")
            return
        
        gasto = self.bico.gastarFolha()

        if self.bico.tamanho <= 10 :
            self.bico = None 
            print("fail: tamanho insuficiente")
            return
        
        novo_tamanho = self.bico.tamanho - gasto

        if novo_tamanho < 10:
            print("fail: folha incompleta")
            self.bico.tamanho = 10  
            return
        self.bico.tamanho = novo_tamanho
        


def main():
    lapinho = None

    while True:
        line = input()
        print("$" + line)
        args = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(lapinho)
        elif args[0] == "init":
            q = float(args[1])
            lapinho = Lapiseira(q)
        elif args[0] == "insert":
            calibre = float(args[1])
            dureza = args[2]
            tamanho = int(args[3])

            grafite = Grafite(calibre, dureza, tamanho)

            if lapinho is None:
                print("fail: lapiseira nao iniciada")
            elif not lapinho.inserir(grafite):
                print("fail: calibre incompatível")
        
        elif args[0] == "pull":
            if lapinho is None:
                print("fail: lapiseira nao iniciada")
            else:
                lapinho.puxar()

        elif args[0] == "remove":
            lapinho.remover()
        elif args[0] == "write":
            lapinho.escrever()

main()