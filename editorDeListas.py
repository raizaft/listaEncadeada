from listaEncadeada import Lista
import os

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def menu(lista):
    while True:
        print("""
Lista = []
Editor de Listas
--------------------
1 - Tamanho
2 - Inserir
3 - Remover
4 - Exibir elemento
5 - Procurar valor
6 - Modificar
7 - Inserir no início
8 - Inserir no fim
9 - Esvaziar
10 - Remover do início
11 - Remover do fim
12 - Remover ocorrências
13 - Sair
        """)
        op = input("Digite sua opção: ")
        
        if op == "1":
            cls()
            print(f'Tamanho da lista: {l.tamanho()}')
        if op == "2":
            cls()
            print("Inserir Elemento")
            p = int(input("Posição: "))
            c = input("Carga: ")
            l.inserir(p,c)
        if op == "3":
            cls()
            print("Remover Elemento")
            p = int(input("Posição: "))
            l.remover(p)
        if op == "4":
            cls()
            print("Exibir Elemento")
            p = int(input("Posição: "))
            print(l.elemento(p))
        if op == "5":
            cls()
            print("Procurar Valor")
            c = input("Chave: ")
            print(l.busca(c))
        if op == "6":
            cls()
            print("Modificar Elemento")
            p = int(input("Posição: "))
            c = input("Nova carga: ")
            l.modificar(p,c)
        if op == "7":
            cls()
            print("Inserir no início")
            c = input("Carga: ")
            l.insereInicio(c)
        if op == "8":
            cls()
            print("Inserir no fim")
            c = input("Carga: ")
            l.insereFim(c)
        if op == "9":
            cls()
            l.esvaziar()
            print("Lista vazia!")
        if op == "10":
            cls()
            l.removeInicio()
        if op == "11":
            cls()
            l.removeFim()
        if op == "12":
            cls()
            print("Remover ocorrências")
            o = input("Carga: ")
            l.removeOcorrencias(o)
        if op == "13":
            cls()
            print("Programa Encerrado!")
            break

l = Lista()

menu(l)

