'''
#paradigma = forma de se resolver problemas em linguagem de programação
#função é pegar algo abstrato e materializar em forma de programação

modelo:

def nome_funcao(parametros):
    comandos
exemplo 1:

def saudacao(nome):
    return(f"boa tarde {nome.title()}!")

nome = input("digite seu nome: ")
resultado = saudacao(nome)
print(resultado)

exemplo 2:

#criar função que recebe nome e idade e retorna uma mensagem de cadastro com o nome e idade informado

def cadastro(n,i):
    return f"O usuário {n} com idade {i} foi cadastrado com sucesso"
nome = input ("digite seu nome: ")
idade = int(input("Digite sua idade:"))
if(idade>45):
    resultado = cadastro (nome, idade)
    print (resultado)
else: print("idade não aceita")
'''

#exercício 1:

def dobro(numero):
    return numero * 2

numero = int(input("digite um número: "))
resultado = dobro(numero)
print(resultado)




