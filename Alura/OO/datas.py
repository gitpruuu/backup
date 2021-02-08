from datetime import date

class Data:
    
    def __init__(self):
        pass
        self.data_atual = date.today().strftime("%d/%m/%Y")
        print(self.data_atual)