import mysql.connector
cnx = mysql.connector.connect(user="root", password="", host="127.0.0.1")
meucursor = cnx.cursor()
from Ex113 import Leituras


def db():
    meucursor.execute("create database if not exists cadastrados;")
    meucursor.execute("use cadastrados;")


def tabelas():
    meucursor.execute("create table if not exists registrados(nome varchar(50), idade int)default charset = utf8;")


def add():
    nome = str(input("Nome: "))
    print("---" * 15)
    idade = Leituras.intput("Idade: ")
    print("---" * 15)
    meucursor.execute(f"insert into registrados value ('{nome}', '{idade}');")
    print("\033[1;32mPessoas Cadastrada com sucesso!!!\033[m")


def escrever(idade=False):
    print()
    if idade is False:
        meucursor.execute("SELECT * FROM registrados;")
        rows = meucursor.fetchall()
        for row in rows:
            print("  -", end="")
            for num, item in enumerate(row):
                if num == 0:
                    print(f"{item:<22}", end="   ")
                else:
                    print(f"{item:>4}", end=" - ")
            print("Idade")
    else:
        meucursor.execute(f"SELECT * FROM registrados order by idade, nome;")
        rows = meucursor.fetchall()
        for row in rows:
            print("  -", end="")
            for num, item in enumerate(row):
                if num == 0:
                    print(f"{item:<22}", end="   ")
                else:
                    print(f"{item:>4}", end=" - ")
            print("Idade")
    print()
