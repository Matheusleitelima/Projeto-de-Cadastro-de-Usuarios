import sqlite3
from modelo import Pessoa
import funcoes
conexao = None


print('Bem vindo ao nosso sistema de Banco de dados')
while True:
    while True:
        print('Escolha as opções abaixo')
        print('1 - Criar e conectar ao banco')
        print('2 - Criar tabela  no banco')
        print('3 - Inserir dados na tabela')
        print('0 - sair')
        try:
            opc_menu = int(input('Digite a opção:'))
            break
        except ValueError:
            print('opção invalidade, tente novamente\n')

    if opc_menu == 1:
        conexao = funcoes.conectar_banco('meu_banco.db')
        print(f'Banco de dados inciado  com sucesso!')

    elif opc_menu == 2:
        try:
            conexao = funcoes.criar_tabela(conexao)
            print('Tabela de clientes criadas !\n')

        except NameError:
            print(
                'error ao criar tabela pois o banco de dados não foi criado, volte ao menu e selecione 1 \n')

    elif opc_menu == 3:
        try:
            conexao = funcoes.inserir_dados(conexao)

        except NameError:
            print(
                'error ao inserir dados pois o banco de dados não foi criado, volte ao menu e selecione 1 \n')

    elif opc_menu == 0:

        if conexao:
            conexao.commit()
            conexao .close()
