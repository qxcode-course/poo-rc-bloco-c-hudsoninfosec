class Kid:
    def __init__(self, name: str, age: int):
        self.name = name 
        self.age = age 

    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
    def setName(self, name : str):
        self.name = name 
    def setAge(self, age: int):
        self.age = age 

    def __str__(self) -> str:
        return f"{self.name}:{self.age}"

class Trampoline:
    def __init__(self):
        self.playing: list[Kid] = []
        self.waiting: list[Kid] = []
    
    def removeFromList(self, name: str, list_k : list[Kid]) -> Kid | None:
        for i, k in enumerate(list_k):
            if k.getName() == name:
                return list_k.pop(i)
        return None 
    
    def removerKid(self, name: str) -> Kid | None:
        kid = self.removeFromList(name, self.waiting)

        if kid is not None:
            return kid 
        return self.removeFromList(name, self.playing)
    
    def arrive(self, kid: Kid):
        self.waiting.insert(0, kid) # inserir um elemento em uma posição especifica da lista

    def enter(self):
        if len(self.waiting) > 0:
            kid = self.waiting.pop(-1)
            self.playing.insert(0, kid)

    def leave(self):
        if len(self.playing) > 0:
            kid = self.playing.pop(-1)
            self.waiting.insert(0, kid)


    def __str__(self) -> str:
        espera = ", ".join(str(x) for x in self.waiting)
        jogar = ", ".join(str(x) for x in self.playing)

        return f"[{espera}] => [{jogar}]"
    
def main():
    pular = Trampoline()

    while True:
        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")


        if args[0] == "end":
            break
        elif args[0] == "show":
            print(pular)
        elif args[0] == "arrive":
            n = args[1]
            a = int(args[2])

            pular.arrive(Kid(n, a))
        elif args[0] == "enter":
            pular.enter()
        elif args[0] == "leave":
            pular.leave()

        elif args[0] == "remove":
            n = args[1]
            kid = pular.removerKid(n)

            if kid is None:
                print(f"fail: {n} nao esta no pula-pula")



main()