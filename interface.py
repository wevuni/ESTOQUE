from tkinter import *
from funçoes import *
#interface
root= Tk()

#criando frame
fr1 = Frame(root)
fr2 = Frame(root)
#              cod= input('Insira o cod')
              #  nome= input('Insira o nome')
                #fabricante= input('Insira o fabricante')
               # quantia= input('Insira a quantia')
#criando label
def __init__(self):
    opcoes = DBAgenda()
    
lb0 = Label(fr1, text='ESTOQUE', font="Calibri 20", pady=30)
bt1 = Button (fr1, text='1 - Cadastrar produto', font="Calibri 14", command= lambda: [fr1.grid_remove(), fr2.grid(row=0, column=0)])
bt2 = Button (fr1, text='2 - Listar produto', font="Calibri 14")
bt3 = Button (fr1, text='3 - Procurar produto(COD)', font="Calibri 14")
cod= Entry (fr1)
bt4 = Button (fr1, text='4 - Alterar produto', font="Calibri 14")
bt5 = Button (fr1, text='5 - Sair', font="Calibri 14")
def salvar_produto(self, nome, fabricante, quantia):
    nome=ent()
    fabricante

lbe=Label(fr2, text='Insira o nome:', font="Calibri 14")
lbe1=Label(fr2, text='Insira o fabricante:', font="Calibri 14")
lbe2=Label(fr2, text='Insira a quantia:', font="Calibri 14")
ent=Entry(fr2)
ent1=Entry(fr2)
ent2=Entry(fr2)

#layout
fr1.grid(row=0, column=0)
lb0.grid(row=0, column=0, sticky=NSEW)
bt1.grid(row=1, column=0, sticky=NSEW)
bt2.grid(row=2, column=0, sticky=NSEW)
bt3.grid(row=3, column=0, sticky=NSEW)
cod.grid(row=3, column=1, sticky=NSEW)
bt4.grid(row=4, column=0, sticky=NSEW)
bt5.grid(row=5, column=0, sticky=NSEW)

lbe.grid(row=0, column=0, sticky=NSEW)
lbe1.grid(row=1, column=0, sticky=NSEW)
lbe2.grid(row=2, column=0, sticky=NSEW)
nome.grid(row=0, column=1)
fabricante.grid(row=1,column=1)
quantia.grid(row=2, column=1)
#mainloop
root.mainloop()
