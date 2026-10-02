# shopping

class ShoppingCart:
    def __init__(self):
        self.checklist = []

    def add(self, item):
        self.checklist.append(item)
        return(f'Товар {item} добавлен.')

    def remove(self, item):
        self.checklist.remove(item)
        return(f'Товар {item} удалён.')

    def items(self):
        return self.checklist