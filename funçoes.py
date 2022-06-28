from info_produto import *
class Opcoes:
    def __init__(self):
        self.listaProdutos=[]

    def cadastrar_produtos(self):
        self.listaProdutos.append(Info_produto())

    def listar_produtos(self):
        for i in range(len(self.listaProdutos)):
            print('Codigo:',self.listaProdutos[i].cod,
            'Descrição(Nome)',self.listaProdutos[i].nome,
            'Fabricante',self.listaProdutos[i].fabricante,
            'Quantidade', self.listaProdutos[i].quantia)
