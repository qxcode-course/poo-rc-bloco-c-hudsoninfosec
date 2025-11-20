class Cliente:
    def __init__(self, id: str, phone: int):
        self.id = id 
        self.phone = phone 
    def __str__(self):
        return f"{self.id}:{self.phone}"
    def getID(self):
        return self.id
    def getPhone(self):
        return self.phone 
    def setID(self, id: str):
        self.id = id 
    def setPhone(self, fone: int):
        self.phone = fone 
class Theather:
    def __init__(self, capacity: int):
        self.__capacity = capacity
        self.__seats: list[Cliente | None] = [None] * capacity
    def search(self, id: str) -> int:
        for i, c in enumerate(self.__seats):
            if c is not None and c.getID() == id:
                return i 
        return -1
    
    def verifyIndex(self, index : int) -> bool:
        return 0 <= index < self.__capacity
    def reserve(self, id: str, phone: int, index: int ) -> bool:
        if index < 0 or index >= len(self.__seats):
            print("fail: cadeira nao existe")
            return False
        elif self.search(id) != -1:
            print("fail: cliente ja esta no cinema")
            return False
        elif self.__seats[index] is not None:
            print("fail: cadeira ja esta ocupada")
            return False
        
        self.__seats[index] = Cliente(id, phone)
        return True 
        
    def cancel(self, id: str) -> bool:
        pos = self.search(id)

        if pos == -1:
            print("fail: cliente nao esta no cinema")
            return True
        
        self.__seats[pos] = None
        return True
    
    def getSesats(self):
        return self.__seats
    
    def __str__(self):
        out = []

        for seats in self.__seats:
            if seats is None:
                out.append("-")
            else:
                out.append(str(seats))
        return f"[{" ".join(out)}]"
def main():
    cine = Theather(0)

    while True:

        line = input()
        print("$" + line)
        args: list[str] = line.split(" ")

        if args[0] == "end":
            break
        elif args[0] == "show":
            print(cine)
        elif args[0] == "init":
            c = int(args[1])

            cine = Theather(c)
        elif args[0] == "reserve":
            sid = args[1]
            fone = int(args[2])
            idx = int(args[3])

            cine.reserve(sid, fone, idx)
        elif args[0] == "cancel":
            id = args[1]
            cine.cancel(id)
        else:
            print("fail: comando nao encontrado")
main()