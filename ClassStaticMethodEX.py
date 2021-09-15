class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients 
    def __repr__(self): #__repr__ method returns object representation in string format
        return f'Pizza({self.ingredients})'
    @classmethod 
    def margherita(cls):
        return cls(['cheese', 'tomatoes'])
    @classmethod
    def proscuto(cls):
        return cls(['cheese','tomatoes', 'ham', 'mushrooms'])
    @staticmethod
    def hasCheese():
        return "the pizza has cheese"
Pizza.margherita()
Pizza.hasCheese()
Pizza.proscuto()
print(Pizza.hasCheese())
print(Pizza.margherita())
print(Pizza.proscuto())