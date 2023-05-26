import random
from time import sleep
from tkinter import *
import tkinter as tk



class start:
    perguntas = [('Qual é a capital do Brasil?', 'Brasília', ['Rio de Janeiro', 'São Paulo', 'Belo Horizonte']),
                ('Qual é o maior animal terrestre?', 'Elefante', ['Girafa', 'Leão', 'Hipopótamo'])
    ]

    def __init__(self, master):
       
        self.master = master
        master.title("Quiz")
        master.geometry('500x500') 
        #principal = Frame(master, padding='10 10 30 30')
        #janela = Frame(principal,)
        self.pergunta_label = tk.Label(master, text="",font='Ariel 20', bd=5, relief='sunken')
    
        self.pergunta_label.pack(fill=Y)
        self.respostas_buttons = []
        for i in range(4):    
            button = tk.Button(master, text="", command=lambda index=i: self.respondendo(index))
            button.pack(fill=X, anchor='s')
            self.respostas_buttons.append(button)
        self.status_label = tk.Label(master, text="")
        self.status_label.pack()
        sleep(2)
        
        # janela.grid()
        # principal.grid()
        self.preparando()


    def preparando(self, *args):
        pergunta_escolhida = random.choice(self.perguntas)
        self.perguntas.remove(pergunta_escolhida)
        self.pergunta = pergunta_escolhida[0]
        self.certa = pergunta_escolhida[1]
        self.opcoes = [item for item in pergunta_escolhida[2] ]
        self.opcoes.insert(random.randint(0, 2), pergunta_escolhida[1])
        self.indice = self.opcoes.index(self.certa) + 1
        self.pergunta_label.config(text=self.pergunta)
        for i in range(4):
            self.respostas_buttons[i].config(text=self.opcoes[i])


    def respondendo(self, index):
        self.res = index + 1
        if self.res == self.indice:
            self.status_label.config(text="Acertou!")
        else:
            self.status_label.config(text="Errou! A resposta correta era: " + self.certa)
        self.preparando()
        self.status_label.after(2000, lambda: self.status_label.config(text=""))
        


root = tk.Tk()
jogo = start(root)
root.mainloop()
