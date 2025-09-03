import sqlite3
from modelo import Pessoa


# CONECTAR
def conectar_banco(nome_banco):
    conexao = sqlite3.connect(nome_banco)
    conexao.execute("PRAGMA foreign_keys = on")
    return conexao


# CRIAR TABELA
def criar_tabela(conexao):
    try:
        cursor = conexao.cursor()

        comando = '''CREATE TABLE IF NOT EXISTS Cadastro(
               CPF char(11) primary key,
               nome varchar(90) not null,
               email varchar(50) unique not null,
               data_nascimento date);'''

        cursor.execute(comando)

        conexao.commit()

    except sqlite3.DatabaseError as err:
        print("Erro de banco de dados:", err)

    finally:
        cursor.close()
        


# INSERIR DADOS
def inserir_dados(conexao):
    registros = []  # lista que vai armazenar as pessoas a inserir
    while True:
        # verificação de cpf
        info_cpf = input(
            'Digite o cpf da pessoa(11 digitos) ou (digite sair):')
        if info_cpf.lower() == 'sair':
            return  # sai da função
        elif len(str(info_cpf)) != 11 or not info_cpf.isdigit():
            print('cpf invalido')
            continue

        info_nome = input('Digite seu nome:').title()
        info_email = input('Digite seu e-mail:').lower()
        info_data = input('Digite sua data de nascimento:')

        pessoa = Pessoa(info_cpf, info_nome, info_email, info_data)

        registros.append({
            "cpf": pessoa.cpf,
            "nome": pessoa.nome,
            "email": pessoa.email,
            "data": pessoa.data_nascimento
        })  # adiciona dentro da lista de registros

        if registros:
            cursor = conexao.cursor()
            comando = '''
                INSERT OR IGNORE INTO Cadastro(cpf, nome, email, data_nascimento)
                VALUES (:cpf, :nome, :email, :data)
            '''  # INSERT OR IGNORE no comando SQL, assim registros com e-mails repetidos são simplesmente ignorados
            cursor.executemany(comando, registros)
            print('dados inseridos com sucessos \n')
            conexao.commit()
            cursor.close()

        else:
            print('nenhum dado inserida')
