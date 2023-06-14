from collections import deque
class Cola:
    def __init__(self):
        self.cola = deque([])

    def __len__(self):
        return len(self.cola)

    def sacar(self):
        return self.cola.popleft()

    def agregar(self, elemento):
        self.cola.append(elemento)
