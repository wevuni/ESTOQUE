from funçoes import *
class classe_menuu:
    def __init__(self):
        opcoes = DBAgenda()
        while True:
            entrada=input('1 - Cadastrar produto\n2 - Listar produtos\n3 - Sair')
            if entrada == '1':
                cod= input('Insira o cod')
                nome= input('Insira o nome')
                fabricante= input('Insira o fabricante')
                quantia= input('Insira a quantia')
                opcoes.cadastrar_produtos(cod, nome, fabricante, quantia)
            elif entrada == '2':
                opcoes.listar_produtos()
            elif entrada == '0':
                break
            else:
                print ('Opção inválida!!!')