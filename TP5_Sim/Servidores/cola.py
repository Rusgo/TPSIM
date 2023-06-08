
class Cola:
    cola=[]

    def __len__(self):
        return len(self.cola)

    def sacar(self):
        return self.cola.pop()

    def agregar(self, elemento):
        self.cola = [elemento] + self.cola
