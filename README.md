
# Sistema de Cadastro com Python e SQLite

## Descrição
Este projeto é um sistema simples de cadastro de pessoas utilizando Python e SQLite.  
Ele permite criar um banco de dados, criar uma tabela de clientes e inserir registros de pessoas com CPF, nome, e-mail e data de nascimento.

---

## Tecnologias Utilizadas
- Python 3.x
- SQLite3

---

## Estrutura do Projeto
```
projeto/
│
├── main.py            # Arquivo principal do sistema
├── funcoes.py         # Funções para manipulação do banco de dados
├── modelo.py          # Classe Pessoa
└── meu_banco.db       # Banco de dados SQLite (gerado pelo sistema)
```

---

## Como Executar

1. Certifique-se de ter o Python instalado em sua máquina.
2. Clone ou baixe este projeto.
3. Navegue até a pasta do projeto via terminal.
4. Execute o arquivo principal:
```bash
python main.py
```

---

## Funcionalidades
- **Criar e conectar ao banco:** Inicializa ou conecta ao banco de dados `meu_banco.db`.
- **Criar tabela de clientes:** Cria a tabela `Cadastro` no banco de dados.
- **Inserir dados:** Permite inserir pessoas no banco, verificando CPF válido e evitando duplicidades de e-mail.
- **Sair do sistema:** Encerra o programa, salvando alterações no banco.

---

## Classe `Pessoa`
Classe que representa um registro de pessoa:

```python
class Pessoa:
    def __init__(self, cpf, nome, email, data_nascimento):
        self.cpf = cpf
        self.nome = nome
        self.email = email
        self.data_nascimento = data_nascimento
```

---

## Observações
- O CPF deve conter 11 dígitos.
- E-mails duplicados são ignorados na inserção.
- Datas devem ser inseridas no formato `AAAA-MM-DD`.

---

## Autor
Matheus
