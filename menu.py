from funçoes import *
class classe_menuu:
    def __init__(self):
        opcoes = Opcoes()
        while True:
            entrada=input('1 - Cadastrar produto\n2 - Listar produtos\n3 - Sair')
            if entrada == '1':
                opcoes.cadastrar_produtos()
            elif entrada == '2':
                opcoes.listar_produtos()
            elif entrada == '0':
                break
            else:
                print ('Opção inválida!!!')